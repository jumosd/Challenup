from django import forms
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User


# class UserForm(UserCreationForm):

#     class Meta:
#         model = User
#         fields = ("username", "password1", "password2")

from .models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        # fields =("userid","nick","name")
        fields ="__all__"

        labels ={
            'userid' : "아이디",
            "nick" : "닉네임",
            "name" : "이름(본명)",
        }
        password = forms.CharField()
        password2 = forms.CharField()

    def clean_password2(self):
        password = self.cleaned_data.get("user_password") # 👈 필드의 입력값 가져오기
        password2 = self.cleaned_data.get("puser_assword2") # 👈 필드의 입력값 가져오기
        if password != password2:
            raise forms.ValidationError("비밀번호가 일치하지 않아요 !!")
        else:
            return password
        
    def save(self):
        first_name = self.cleaned_data.get("first_name")
        last_name = self.cleaned_data.get("last_name")
        password = self.cleaned_data.get("password")
        # create_user()에 id(email), email(email), password(password) 값을 순서대로 넣어줘요!
        user = models.User.objects.create_user(email, email, password)
        user.first_name = first_name
        user.last_name = last_name
        user.save()     