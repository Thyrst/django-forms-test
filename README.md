# django-forms-test
Module to simplify testing forms in Django framework

## Installation

You can simply install it with use of `pip`:

`pip install git+https://github.com/Thyrst/django-forms-test.git`

Then you'll import it into your testing script like this:

`from django_forms_test import field, cleaned, FormTest`

## Usage

You will create a subclass of `FormTest` which is subclass of `django.test.TestCase`, so you can add tests as you are used to. To the attribute `form` you assign class of the form you are testing. `required_fields` should be a list of fields required by your form.

```python
class YourClass(FormTest):
    form = YourForm
    required_fields = ['email', 'message']
```

Instead of the name of a field you can use a tuple of name and field type. Available field types are `URL`, `TEXT`, `PASSWORD`, `USERNAME`, `EMAIL`. Field types serves to additional checking of permitted field value (e.g. a form shouldn't accept an invalid URL). The `TEXT` is the default type and has no additional verifications.

```python
class YourClass(FormTest):
    form = YourForm
    required_fields = [('email', field.EMAIL), 'message'] # same as ('message', field.TEXT)
```

For testing of form's cleaning methods you can use a decorator `cleaned` which accepts the input field values as arguments and passes them cleaned to your function.

```python
class YourClass(FormTest):
    form = YourForm
    
    @cleaned(nick='  Bob ')
    def test_strip_nick(self, nick):
        self.assertEqual(nick, 'Bob')
```

## Example

You code this:

```python
class SaveFormTest(FormTest):
    form = SaveForm
    required_fields = ['title', 'tags', ('url', field.URL)]

    @cleaned(tags='one, two')
    def test_cleaning_tags(self, tags):
        self.assertIsInstance(tags, list)
        self.assertEqual(len(tags), 2)
        self.assertEqual(tags[1], 'two')

    @cleaned(description='')
    def test_cleaning_description(self, description):
        self.assertIsNone(description)
```

Instead of this:

```python
class SaveFormTest(TestCase):

    data = {
        'title': 'some title',
        'url': 'http://some.url',
        'tags': 'some tags',
    }

    def test_valid_form(self):
        form = SaveForm(self.data)
        self.assertTrue(form.is_valid())

    def test_invalid_url(self):
        my_data = copy(self.data)
        my_data['url'] = 'invalid url'
        form = SaveForm(my_data)

        self.assertFalse(form.is_valid())

    def test_required_fields(self):
        for field in ('title', 'url', 'tags'):
            with self.subTest(field=field):
                my_data = copy(self.data)
                my_data[field] = ''
                form = SaveForm(my_data)

                self.assertFalse(form.is_valid())

    def test_cleaning_tags(self):
        form = SaveForm({'tags': 'one, two'})
        form.is_valid()

        tags = form.cleaned_data['tags']
        self.assertIsInstance(tags, list)
        self.assertEqual(len(tags), 2)
        self.assertEqual(tags[1], 'two')

    def test_cleaning_description(self):
        form = SaveForm({'description': ''})
        form.is_valid()

        description = form.cleaned_data['description']
        self.assertIsNone(description)

```

And you code this:

```python
class RegisterFormTest(FormTest):
    form = RegisterForm
    required_fields = [
        ('username', field.USERNAME),
        ('email', field.EMAIL),
        ('password', field.PASSWORD),
        ('confirm_password', field.PASSWORD),
    ]
```

Instead of this:

```python
class RegisterFormTest(TestCase):

    data = {
        'username': 'some_username',
        'email': 'some@email.com',
        'password': 'some password',
        'confirm_password': 'some password',
    }

    def test_valid_form(self):
        form = RegisterForm(self.data)
        self.assertTrue(form.is_valid())

    def test_invalid_username(self):
        my_data = copy(self.data)
        my_data['email'] = 'invalid email'
        form = RegisterForm(my_data)

        self.assertFalse(form.is_valid())

    def test_invalid_email(self):
        my_data = copy(self.data)
        my_data['email'] = 'invalid email'
        form = RegisterForm(my_data)

        self.assertFalse(form.is_valid())

    def test_required_fields(self):
        for field in ('username', 'email', 'password', 'confirm_password'):
            with self.subTest(field=field):
                my_data = copy(self.data)
                my_data[field] = ''
                form = RegisterForm(my_data)

                self.assertFalse(form.is_valid())

    def test_password_safe_input(self):
        form = RegisterForm()
        input_type = form['password'].field.widget.input_type
        self.assertEqual(input_type, 'password')

        input_type = form['confirm_password'].field.widget.input_type
        self.assertEqual(input_type, 'password')
        
  ```
  ## Announcement
  
  I've done this just for my personal use, so there are many things that are still missing and I probably won't implement them until I need them. However feel free to send a pull request if you miss something.
  
