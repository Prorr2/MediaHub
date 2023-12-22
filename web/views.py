from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.contrib.auth import authenticate
from .forms import UserForm, ProfileForm, PostForm, CommentForm, MessageForm
from .models import Profile, UserPost, Comment, Message
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login
from django.contrib.auth.models import User
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
                auth_login(request, user)
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
def crearPost(request):
     form = PostForm()
     if request.method == 'POST':
          form = PostForm(request.POST, request.FILES)
          if form.is_valid():
            media = form.cleaned_data.get("media")
            description = form.cleaned_data.get("description")
            profile = Profile.objects.get(user = request.user)
            UserPost.objects.create(media = media, description = description, profile = profile)
     return render(request, "crearPost.html", {"Form" : form})
class Posts(ListView):
     template_name = "posts.html"
     context_object_name = "Posts"
     def get_queryset(self) -> QuerySet[Any]:
          profile = Profile.objects.get_or_create(user = self.request.user)
          return UserPost.objects.all()
     def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
          context = super().get_context_data(**kwargs)
          context["Profile"] = Profile.objects.get(user = self.request.user)
          context["User"] = self.request.user
          context["CommentForm"] = CommentForm()
          return context
def sendComment(request):
     if request.POST:
          form = CommentForm(request.POST)
          if form.is_valid():
               (profile, _) = Profile.objects.get_or_create(user = request.user)
               id = int(request.POST.get("id"))
               print(id)
               Comment.objects.create(content = form.cleaned_data.get("content"), post = UserPost.objects.get(id = 
            id), profile = profile)
     return redirect('web:posts')
class people_messages(ListView):
     template_name = "messages.html"
     context_object_name = "Profiles"
     model = Profile

class dm(ListView):
     template_name = "dm.html"
     context_object_name = "Messages"
     def get_queryset(self) -> QuerySet[Any]:
          print(self.kwargs["username"])
          user_to = User.objects.get(username = self.kwargs["username"])
          profile_to = Profile.objects.get(user = user_to)
          profile_from = Profile.objects.get(user = self.request.user)
          communication1= Message.objects.filter(profile_to = profile_to, profile_from = profile_from)
          communication2 = Message.objects.filter(profile_to = profile_from, profile_from = profile_to)
          return communication1.union(communication2) #bidirectional communication
     def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
          context = super().get_context_data(**kwargs)
          context["Form"] = MessageForm()
          context["profile_to"] = self.kwargs["username"]
          return context
     
def sendMessage(request):
     if request.POST:
          form = MessageForm(request.POST)
          if form.is_valid():
               (profile_from, _) = Profile.objects.get_or_create(user = request.user)
               (profile_to, _) = Profile.objects.get_or_create(user = User.objects.get(username = request.POST.get("profile_to")))
               print(id)
               Message.objects.create(content = form.cleaned_data.get("content"), profile_from = profile_from, profile_to = profile_to)
     return redirect('web:dm/' + request.POST.get("profile_to"))