from django import forms
from django.core.exceptions import ValidationError
from apps.users.models import CustomUser


class RegisterUserForm(forms.ModelForm):
    repeat_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Сюда'}),
        label="Повторите пароль"
    )

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        repeat_password = cleaned_data.pop('repeat_password')
        if password != repeat_password:
            raise ValidationError(
                "Пароли не совпадают"
            )
        if CustomUser.objects.filter(email=cleaned_data.get('email')):
            raise ValidationError('Пользователь уже есть')

    class Meta:
        model = CustomUser
        fields = [
            'email',
            'password',
        ]


class AvtorizateUser(forms.Form):
    email = forms.CharField(max_length=255)
    password = forms.CharField(widget=forms.PasswordInput())
