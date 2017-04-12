# django-forms-test
Module to simplify testing forms in Django framework

## Installation

You can simply install it with use of `pip`:

`pip install git+https://github.com/Thyrst/django-forms-test.git`

Then you'll import it into your testing script like this:

`from django_forms_test import field, cleaned, FormTest`

## Example

You code this:

```python
class LoginFormTest(FormTest):
    form = LoginForm
    required_fields = ['username', ('password', field.PASSWORD)]
```

Instead of this:

```python
class LoginFormTest(TestCase):
    data = {
        'username': 'some username',
        'password': 'some password',
    }

    def test_valid_form(self):
        form = LoginForm(self.data)
        self.assertTrue(form.is_valid())

    def test_required_fields(self):
        for field in ('username', 'password'):
            with self.subTest(field=field):
                my_data = copy(self.data)
                my_data[field] = ''
                form = LoginForm(my_data)

                self.assertFalse(form.is_valid())

    def test_password_safe_input(self):
        form = LoginForm()
        input_type = form['password'].field.widget.input_type

        self.assertEqual(input_type, 'password')
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
  
