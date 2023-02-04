from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["nickname","username","password"]

        labels ={
            'nickname' : "닉네임",
            "username" : "아이디",
            "password" : "비밀번호",
        }
        password = forms.CharField()
        password2 = forms.CharField()

    # def clean_password2(self):
    #     password = self.cleaned_data.get("user_password") # 👈 필드의 입력값 가져오기
    #     password2 = self.cleaned_data.get("puser_assword2") # 👈 필드의 입력값 가져오기
    #     if password != password2:
    #         raise forms.ValidationError("비밀번호가 일치하지 않아요 !!")
    #     else:
    #         return password
        
 