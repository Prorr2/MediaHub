from django import forms
from .models import Profile, UserPost, Comment, Message
inputclass = "p-2 rounded-sm"
textareaclass = "p-2 rounded-sm"
class iconCustomWidget(forms.ClearableFileInput):
    template_name = "custom_widgets/iconInput.html"
class aliasCustomWidget(forms.TextInput):
    template_name = "custom_widgets/aliasInput.html"
class mediaCustomWidget(forms.ClearableFileInput):
    template_name = "custom_widgets/mediaInput.html"   

class UserForm(forms.Form):
    username = forms.CharField(label="", max_length=50, widget=forms.TextInput(attrs={"class" : inputclass, "placeholder" : "Usuario"}))
    password = forms.CharField(label="",widget=forms.PasswordInput(attrs={"class" : inputclass, "placeholder" : "Contraseña"}), max_length=50)
class ProfileForm(forms.ModelForm):
    icon = forms.ImageField(label="", widget=iconCustomWidget)
    alias = forms.CharField(label = "", widget=aliasCustomWidget)
    description = forms.CharField(label="", max_length=2000, widget=forms.Textarea(attrs={"placeholder" : "Descripción", "class" : textareaclass}))
    class Meta:
        model = Profile
        fields = ['icon','alias', 'description']
class PostForm(forms.ModelForm):
    media = forms.FileField(label= "", widget=mediaCustomWidget)
    description = forms.CharField(label="", max_length=2000, widget=forms.Textarea(attrs={"placeholder" : "Descripción", "class" : textareaclass}))
    class Meta:
        model = UserPost
        fields = ["media", "description"]

class CommentForm(forms.ModelForm):
    content = forms.CharField(label="", max_length=2000, widget=forms.Textarea(attrs={"placeholder" : "Comentario", "class" : "p-5 w-72", "style" : "height: 120px; margin-top: 50px"}))
    class Meta:
        model = Comment
        fields = ["content"]

class MessageForm(forms.ModelForm):
    content = forms.CharField(label="", max_length=2000, widget=forms.Textarea(attrs={"placeholder" : "Mensaje", "class" : "p-5 w-[70rem] rounded-full", "style" : "height: 50px; margin-top: 50px"}))
    class Meta:
        model = Message
        fields = ["content"]