from django.core.exceptions import ValidationError
import string
from django.core.validators import RegexValidator


def validate_ukr(value, field_label="Поле"):
    allowed_chars = [' ', '-']
    for char in value:
        if char in allowed_chars:
            continue
        elif char.isdigit():
            raise ValidationError(f"{field_label} не должно содержать цифры.")
        elif char in string.punctuation:
            raise ValidationError(f"{field_label} не должно содержать спец. символы.")
        elif char.isalpha():
            if not ('А' <= char <= 'я' or char in 'ЁёІіЇїЄєҐґ'):
                raise ValidationError(f"{field_label} должно содержать только кириллические буквы.")
        else:
            raise ValidationError(f"{field_label}: недопустимый символ.")
    return value


ukrainian_name_validator = RegexValidator(
    regex=r'^[А-ЩЬЮЯЄІЇҐа-щьюяєіїґ\- ]+$',
    message="Фамилия должна содержать только украинские буквы, пробел или дефис."
)

phone_validator = RegexValidator(
    regex=r'^\+380\d{9}$',
    message='Телефон должен быть в формате +380XXXXXXXXX.'
)
