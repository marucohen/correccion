from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class BuscaCursoForm(forms.Form):
    curso = forms.CharField()

class RegistroUsuarioForm(UserCreationForm):
    email = forms.EmailField(label='Correo')
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k:"" for k in fields}

class EditarUsiarioForm(forms.Form):
    email = forms.EmailField(required=False)
    first_name = forms.CharField(label='Nombre', max_length=30, required=False)
    last_name = forms.CharField(label='Apellido', max_length=30, required=False)
    avatar = forms.ImageField(required=False)