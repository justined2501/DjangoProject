from .models import User
from django.forms import ModelForm, Textarea, TextInput, Form


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['name', 'surname', 'patronymic', 'post', 'number', 'email']
        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',

            }),
            "surname": TextInput(attrs={
                'class': 'form-control',

            }),
            "patronymic": TextInput(attrs={
                'class': 'form-control',

            }),
            "post": TextInput(attrs={
                'class': 'form-control',

            }),
            "number": TextInput(attrs={
                'class': 'form-control',

            }),
            "email": TextInput(attrs={
                'class': 'form-control',
            }),
        }


# class AutoForm(Form):
#
