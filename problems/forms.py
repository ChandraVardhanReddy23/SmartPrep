from django import forms
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['codeforces_handle', 'leetcode_handle']
from django.contrib.auth.models import User
from django import forms
from .models import UserProfile
class UserRegisterForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    codeforces_handle = forms.CharField(required=False)
    leetcode_handle = forms.CharField(required=False)
