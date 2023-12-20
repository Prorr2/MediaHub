from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.contrib.auth import authenticate
from .forms import UserForm, ProfileForm, PostForm
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
     try:
        profile = Profile.objects.get(user = request.user)
     except Profile.DoesNotExist:
          profile = None
     if request.method == 'POST':
          try:
              profile_exist = Profile.objects.get(user = request.user)
          except Profile.DoesNotExist:
              profile_exist = None
          form = ProfileForm(request.POST, request.FILES)
          if profile_exist == None:
            if form.is_valid():
                form.save()
          else:
                    form.is_valid() #its does not matter if the form is invalid
                    profile_exist.alias = form.cleaned_data.get("alias")
                    profile_exist.description = form.cleaned_data.get("description")
                    if not form.cleaned_data.get("icon") == None:
                        profile_exist.icon = form.cleaned_data.get("icon")
                    profile_exist.save()
                    return redirect('web:profile')
     return render(request, "profile.html", {"Form" : form, "profile" : profile})
def posts(request):
     form = PostForm()
     return render(request, "posts.html", {"Form" : form})