# from django import forms
# from django.contrib.auth.forms import UserCreationForm, UserChangeForm

# from .models import CustomUser

# class CustomUserCreationForm(UserCreationForm):

#     class Meta:
#         model = CustomUser
#         fields = ("username", "email")

# class CustomUserChangeForm(UserChangeForm):

#     class Meta:
#         model = CustomUser
#         fields = ("username", "email")

from django import forms
from django.contrib.auth.models import User
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from django import forms
from django import forms
from .models import PublicPost, UserPost
 
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    phone_no = forms.CharField(max_length = 20)
    first_name = forms.CharField(max_length = 20)
    last_name = forms.CharField(max_length = 20)
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'phone_no', 'password1', 'password2']


class PublicPostForm(forms.ModelForm):
    class Meta:
        model = PublicPost
        fields = ['title', 'content']
        widgets = {
            'content': SummernoteWidget()
        }

class UserPostForm(forms.ModelForm):
    class Meta:
        model = UserPost
        fields = ['title', 'content']
        widgets = {
            'content': SummernoteWidget()
        }