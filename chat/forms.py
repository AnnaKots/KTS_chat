from django import forms
from django.contrib.auth.forms import AuthenticationForm, UsernameField, UserCreationForm

from chat.models import Message


class LoginForm(forms.Form):
    """ Base class for authenticating users. Extend this to get a form that accepts
    username/password logins. """
    username = UsernameField(
        label='Логин',
        max_length=254,
        widget=forms.TextInput(attrs={'autofocus': True, 'class': 'form-control'}),
    )
    password = forms.CharField(
        label='Пароль',
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )


class MessageCreateForm(forms.ModelForm):
    class Meta:
        model = Message  # создали объект Message
        fields = ['text', ]

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super().__init__(*args, **kwargs)
        self.user = user

    def save(self, commit=True):
        message = super().save(commit=False)  # типо не сохраняем, иначе была бы ошибка
        # так как удалили пользователя, отправляюшего сообщение
        # save модели
        message.author = self.user
        if commit:
            message.save()
        return message


class ChatRegistrationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})
