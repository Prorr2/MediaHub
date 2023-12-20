from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.contrib.auth import authenticate
from .forms import UserForm, ProfileForm
from .models import Profile
# Create your views here.
def login(request : HttpRequest):
    form = UserForm()
    if request.user.is_authenticated:
                return redirect('web:home')
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = authenticate(request, username = form.cleaned_data.get("username"), password = form.cleaned_data.get("password"))
            if user.is_authenticated:
                return redirect('web:home')
    return render(request, "registrer/login.html", {"Form" : form})
def home(request : HttpRequest):
    profile = None
    try:
        profile = Profile.objects.get(user = request.user)
    except Profile.DoesNotExist:
         pass
    return render(request, "home.html", {"profile" : profile})
def profile(request : HttpRequest):
     form = ProfileForm()
     if request.method == 'POST':
          form = ProfileForm(request.POST, request.FILES)
          if form.is_valid():
               form.save()
     return render(request, "profile.html", {"Form" : form})