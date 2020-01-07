from django import forms
from .models import UserProfileInfo
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    username = forms.CharField(
        max_length=50,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Entry No'
            }
        )
    )
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
                'placeholder': 'Password'
            }
        )
    )
    email = forms.EmailField(
        max_length=254,
        widget=forms.EmailInput(attrs={'placeholder': 'Email Address'})
    )
    class Meta():
        model = User
        fields = ('username','password','email')
class UserProfileInfoForm(forms.ModelForm):
    name = forms.CharField(
        max_length=50,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Name'
            }
        )
    )
    cgpa = forms.FloatField(
        widget=forms.NumberInput(
            attrs={
                'placeholder': 'CGPA'
            }
        )
    )
    class Meta():
        model = UserProfileInfo
        fields = ('name','yearofpassing','resume','cgpa')