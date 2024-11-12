from django import forms
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm 
from django.contrib import messages


@login_required
def home(request):
    return render(request, "home.html", {})

def authView(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)  # Use o formulário personalizado
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.email  # Usa o email como nome de usuário
            user.save()
            messages.success(request, "Cadastro realizado com sucesso!")
            return redirect("access:login")
    else:
        form = CustomUserCreationForm()  # Use o formulário personalizado
    return render(request, "registration/signup.html", {"form": form})
