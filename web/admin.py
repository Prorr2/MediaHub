from django.contrib import admin
from .models import Profile, UserPost, Comment, Message
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
# Register your models here.
class CommentInline(admin.StackedInline):
    model = Comment
    can_delete = False
    verbose_name_plural = 'Comments'
class PostInline(admin.StackedInline):
    model = UserPost
    can_delete = False
    verbose_name_plural = 'Posts'
class CommentConfig(admin.ModelAdmin):
    fieldsets = [
        ("Del Perfil", {"fields" : ["profile"]}),
        ("Post ligado", {"fields" : ["post"]}),
        ("Content", {"fields" : ["content"]}),
    ]
class ProfileConfig(admin.ModelAdmin):
    fieldsets = [
        ("User ligado", {"fields" : ["user", "icon"]}),
        ("Alias", {"fields" : ["alias"]}),
        ("Descripción", {"fields" : ["description"]})
    ]
    inlines = (PostInline, )
class UserPostConfig(admin.ModelAdmin):
    fieldsets = [
        ("User Profile", {"fields" : ["profile"]}),
        ("Media", {"fields" : ["media"]}),
        ("Description", {"fields" : ["description"]})
    ]
    inlines = (CommentInline, )
class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profiles'
class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline, )
admin.site.register(Profile, ProfileConfig)
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
admin.site.register(UserPost, UserPostConfig)
admin.site.register(Comment, CommentConfig)
admin.site.register(Message)