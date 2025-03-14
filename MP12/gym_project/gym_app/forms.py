from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from gym_trainer.models import Schedule, Routine
from django import forms
from .models import User

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['email', 'username', 'first_name', 'last_name', 'role', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        try:
            if User.objects.filter(email=email).exists():
                raise ValidationError("Aquest correu ja está registrat.")
        except Exception as e:
            raise ValidationError("Aquest correu ja está registrat.")
        return email

    def clean_username(self):
        username = self.cleaned_data.get('username')
        try:
            if User.objects.filter(username=username).exists():
                raise ValidationError("Aquest nom d'usuari ja està agafat.")
        except Exception as e:
            raise ValidationError("Aquest nom d'usuari ja està agafat.")
        return username
        
class UserLoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [ 'username', 'email', 'first_name', 'last_name']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Afegim classes per  l'estil i plachefolders
        for fields in self.fields:
            self.fields[fields].widget.attrs.update({'class': 'form-control', 'placeholder': self.fields[fields].label})
            
