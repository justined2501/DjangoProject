from datetime import datetime

from django import forms

from worker.models import User


class SalesFilterForm(forms.Form):
    worker = forms.ModelChoiceField(queryset=User.objects.all(), required=False)
    date = forms.CharField(required=False, label="За определенную дату")
    date_from = forms.CharField(required=False)
    date_to = forms.CharField(required=False)

    def clean_date(self):
        date: str = self.cleaned_data.get("date")
        if date:
            try:
                date_obj: datetime.datetime = datetime.strptime(date, '%Y-%m-%d')
                return date_obj
            except ValueError:
                raise forms.ValidationError("Неверный формат даты. Используйте формат гггг-мм-дд.")

        return None

    def clean_date_from(self):
        date_from = self.cleaned_data.get("date_from")
        if date_from:
            try:
                date_obj = datetime.strptime(date_from, '%Y-%m-%d')
                return date_obj
            except ValueError:
                raise forms.ValidationError("Неверный формат даты. Используйте формат гггг-мм-дд.")

        return None

    def clean_date_to(self):
        date_to = self.cleaned_data.get("date_to")
        if date_to:
            try:
                date_obj = datetime.strptime(date_to, '%Y-%m-%d')
                return date_obj
            except ValueError:
                raise forms.ValidationError("Неверный формат даты. Используйте формат гггг-мм-дд.")

        return None
