from django import forms
from django.contrib.auth.forms import UserCreationForm

from account.models import UserProfile


class UserProfileCreateForm(UserCreationForm):
    class Meta:
        model = UserProfile
        fields = ['username', 'first_name', 'last_name', 'patronymic', 'post', 'number', 'email']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'patronymic': forms.TextInput(attrs={'class': 'form-control'}),
            'post': forms.TextInput(attrs={'class': 'form-control'}),
            'number': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }


class UserProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'patronymic', 'post', 'number', 'email']
