from django import forms
inputclass = "p-2 rounded-sm"
textareaclass = "p-2 rounded-sm"
class UserForm(forms.Form):
    username = forms.CharField(label="", max_length=50, widget=forms.TextInput(attrs={"class" : inputclass, "placeholder" : "Usuario"}))
    password = forms.CharField(label="",widget=forms.PasswordInput(attrs={"class" : inputclass, "placeholder" : "Contraseña"}), max_length=50)
class ProfileForm(forms.Form):
    icon = forms.ImageField(label="")
    description = forms.CharField(label="", max_length=2000, widget=forms.Textarea(attrs={"placeholder" : "Descripción", "class" : textareaclass}))