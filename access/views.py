from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

@login_required
def login(request):
    return render(request, "login.html", {})


def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect("access:login")
    else:
        form = UserCreationForm()
    return render(request, "signup.html", {"form": form})

