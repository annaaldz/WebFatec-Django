from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django.core.exceptions import ValidationError

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Email')  # Define o rótulo 'Email'
    password1 = forms.CharField(
        label='Senha',  # Define o rótulo como "Senha"
        widget=forms.PasswordInput,
        help_text="Sua senha deve conter pelo menos 8 caracteres."
    )
    password2 = forms.CharField(
        label='Confirmar senha',  # Define o rótulo como "Confirmação de Senha"
        widget=forms.PasswordInput,
        help_text="Digite a mesma senha novamente."
    )

    class Meta:
        model = CustomUser
        fields = ('email', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if CustomUser.objects.filter(email=email).exists():  # Corrigido para CustomUser
            raise ValidationError("Este email já está em uso.")
        return email

    # Adicionando validação personalizada para a senha
    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        if len(password1) < 8:
            raise ValidationError("A senha deve ter pelo menos 8 caracteres.")
        return password1
