# Подключаем компонент для работы с формой
from django import forms
# Подключаем компонент UserCreationForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# Подключаем модель User
from django.contrib.auth.models import User
from django.forms import Textarea, TextInput, ModelForm

# Создаём класс формы
class RegistrForm(UserCreationForm):
    # Добавляем новое поле Email
    email = forms.EmailField(max_length=254, widget=forms.TextInput(attrs={'placeholder': 'Введите email',
                                                                           'id': 'user_email_inp'}))
    username = forms.CharField(max_length=15, widget=forms.TextInput(attrs={'placeholder': 'Введите имя нового пользователя',
                                                                            'id': 'user_username_inp'}))
    password1 = forms.CharField(max_length=254, widget=forms.PasswordInput(attrs={'placeholder': 'Введите пароль',
                                                                                  'id': 'user_pass1_inp'}))
    password2 = forms.CharField(max_length=254, widget=forms.PasswordInput(attrs={'placeholder': 'Подтвердите пароль',
                                                                                 'id': 'user_pass2_inp'}))

    # Создаём класс Meta
    class Meta:
        # Свойство модели User
        model = User
        # Свойство назначения полей
        fields = ('username', 'email', 'password1', 'password2')

class Confirmation_code(forms.Form):
    auth_code = forms.CharField(label='Код подтверждения', widget=forms.TextInput(attrs={'class': 'form-input'}))