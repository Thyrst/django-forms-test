from copy import copy


def cleaned(**data):
    def decorator(func):
        def wrapper(self):
            form = self.form(data)
            form.is_valid()

            for field in data:
                data[field] = form.cleaned_data[field]

            func(self, **data)

        return wrapper
    return decorator


class FormTestMeta(type):

    def test_required_fields(self):
        for field_ in self.data:
            with self.subTest(field=field_):
                my_data = copy(self.data)
                my_data[field_] = ''
                form = self.form(my_data)

                self.assertFalse(form.is_valid())

    def test_valid_form(self):
        form = self.form(self.data)
        self.assertTrue(form.is_valid())


    def __new__(mcs, name, bases, attrs, **kwargs):
        check = {}
        required_fields = {}
        for field_ in attrs['required_fields']:
            if isinstance(field_, tuple):
                field_name = field_[0]
                field_obj = field_[1]

                check[field_name] = field_obj
                required_fields[field_name] = field_obj.sample
            else:
                required_fields[field_] = field.TEXT.sample

        del attrs['required_fields']
        attrs['data'] = required_fields
        attrs['test_valid_form'] = mcs.test_valid_form
        attrs['test_required_fields'] = mcs.test_required_fields

        for field_name, field_obj in check.items():
            if hasattr(field_obj, 'invalid'):
                def test_invalid(self, field_name=field_name, field_obj=field_obj):
                    my_data = copy(self.data)
                    my_data[field_name] = field_obj.invalid
                    form = self.form(my_data)

                    self.assertFalse(form.is_valid())

                attrs['test_invalid_' + field_name] = test_invalid

            if hasattr(field_obj, 'input_type'):
                def test_input_type(self, field_name=field_name, field_obj=field_obj):
                    form = self.form()
                    input_type = form[field_name].field.widget.input_type
                    self.assertEqual(input_type, field_obj.input_type)

                attrs['test_input_type_' + field_name] = test_input_type

        return super().__new__(mcs, name, bases, attrs)


class field:
    class URL:
        sample = 'http://some.url'
        invalid = 'invalid url'

    class TEXT:
        sample = 'some text'

    class PASSWORD:
        sample = 'some password'
        input_type = 'password'

    class EMAIL:
        sample = 'some@email.com'
        invalid = 'invalid email'

    class USERNAME:
        sample = 'some_username'
        invalid = 'invalid username'
