from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from main.constant_for_app import validate_ukr, ukrainian_name_validator, phone_validator
from account.models import UserProfile



class UserProfileCreateForm(UserCreationForm):
    class Meta:
        model = UserProfile
        fields = ['username', 'first_name', 'last_name', 'middle_name', 'position', 'phone', 'email']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'middle_name': forms.TextInput(attrs={'class': 'form-control'}),
            'position': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }


class UserProfileUpdateForm(forms.ModelForm):
    first_name = forms.CharField(
        max_length=256,
        min_length=4,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )
    last_name = forms.CharField(
        max_length=256,
        min_length=4,
        required=True,
        validators=[ukrainian_name_validator],
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )
    middle_name = forms.CharField(
        max_length=256,
        min_length=4,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )
    phone = forms.CharField(
        max_length=13,
        min_length=10,
        required=True,
        validators=[phone_validator],
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'class': 'form-control'}),
    )

    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'middle_name', 'position', 'phone', 'email', 'image']
        widgets = {
            'position': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }


    def clean_first_name(self):
        value = self.cleaned_data['first_name']
        if value:
            return validate_ukr(value, 'first_name')
        return value


    def clean_last_name(self):
        value = self.cleaned_data['last_name']
        if value:
            return validate_ukr(value, 'last_name')
        return value

    def clean_middle_name(self):
        value = self.cleaned_data['middle_name']
        if value:
            validate_ukr(value, 'middle_name')
        return value


    def clean_image(self):
        image = self.cleaned_data['image']
        if image:
            if image.size > 2 * 1024 * 1024:
                raise ValidationError("файл слишком большой, загрузите файл до 2 мб ")
            if not image.name.endswith(('.jpg', '.png', '.jpeg')):
                raise ValidationError("формат фото неправильный, выберите формат .jpg, .png, .jpeg")
        return image




