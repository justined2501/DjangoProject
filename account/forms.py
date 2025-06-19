from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
import string
from account.models import UserProfile
from django.core.validators import RegexValidator

ukrainian_name_validator = RegexValidator(
    regex=r'^[А-ЩЬЮЯЄІЇҐа-щьюяєіїґ\- ]+$',
    message="Фамилия должна содержать только украинские буквы, пробел или дефис."
)

phone_validator = RegexValidator(
    regex=r'^\+380\d{9}$',
    message='Телефон должен быть в формате +380XXXXXXXXX.'
)

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
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )
    last_name = forms.CharField(
        max_length=256,
        required=True,
        validators=[ukrainian_name_validator],
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )
    middle_name = forms.CharField(
        max_length=256,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )
    phone = forms.CharField(
        max_length=13,
        min_length=10,
        required=True,
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


    def _validate_ukr(self, value, field_label):
        allowed_chars = [' ', '-']
        for char in value:
            if char in allowed_chars:
                continue
            elif char.isdigit():
                raise ValidationError(f"{field_label} не должно содержать цифры")
            elif char in string.punctuation:
                raise ValidationError(f"{field_label} не должно содержать спец символы.")
            elif char.isalpha():
                if not ('А' <= char <= 'я' or char in 'ЁёІіЇїЄєҐґ'):
                    raise ValidationError(f"{field_label} должно содержать только кириллические буквы")
            else:
                raise ValidationError(f"{field_label}: недопустимый символ")
        return value


    def clean_first_name(self):
        value = self.cleaned_data['first_name']
        return self._validate_ukr(value, 'first_name')



    def clean_last_name(self):
        value = self.cleaned_data['last_name']
        return self._validate_ukr(value, 'last_name')



    def clean_middle_name(self):
        value = self.cleaned_data['middle_name']
        return self._validate_ukr(value, 'middle_name')



    def clean_image(self):
        image = self.cleaned_data['image']
        if image:
            if image.size > 2 * 1024 * 1024:
                raise ValidationError("файл слишком большой, загрузите файл до 2 мб ")
            if not image.name.endswith(('.jpg', '.png', '.jpeg')):
                raise ValidationError("формат фото неправильный, выберите формат .jpg, .png, .jpeg")
        return image




