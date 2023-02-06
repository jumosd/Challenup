from django import forms
from django.forms import ModelForm
from .models import User
from django.contrib.auth.forms import UserCreationForm

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username","nickname","password1","password2"]
        labels={
            "username" : "아이디",
            "nickname" : "닉네임",
        }
    

    # def clean_password2(self):
    #     password = self.cleaned_data.get("user_password") # 👈 필드의 입력값 가져오기
    #     password2 = self.cleaned_data.get("puser_assword2") # 👈 필드의 입력값 가져오기
    #     if password != password2:
    #         raise forms.ValidationError("비밀번호가 일치하지 않아요 !!")
    #     else:
    #         return password
        
 
class LoginForm(ModelForm):
    class Meta:
        model = User
        fields=[
            "username", "password"
        ]
        widgets = {'password':forms.PasswordInput}
        labels={
            "username": "아이디",
            "password": "비밀번호",
        }

