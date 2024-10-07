from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    return render(request, "home.html", {})


def authView(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect("access:login")
    else:
        form = UserCreationForm()
    return render(request, "registration/signup.html", {"form": form})

