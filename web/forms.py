from django import forms
from .models import Profile
inputclass = "p-2 rounded-sm"
textareaclass = "p-2 rounded-sm"
class customWidget(forms.ClearableFileInput):
    template_name = "custom_widgets/iconInput.html"
class UserForm(forms.Form):
    username = forms.CharField(label="", max_length=50, widget=forms.TextInput(attrs={"class" : inputclass, "placeholder" : "Usuario"}))
    password = forms.CharField(label="",widget=forms.PasswordInput(attrs={"class" : inputclass, "placeholder" : "Contraseña"}), max_length=50)
class ProfileForm(forms.ModelForm):
    icon = forms.ImageField(label="", widget=customWidget)
    description = forms.CharField(label="", max_length=2000, widget=forms.Textarea(attrs={"placeholder" : "Descripción", "class" : textareaclass}))
    class Meta:
        model = Profile
        fields = ['icon', 'description']