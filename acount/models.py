from django.db import models
from django.core.validators import MinLengthValidator
# Create your models here.

class User(models.Model):
    userid = models.CharField(max_length=20, unique=True,error_messages={'unique' : "이미 존재하는 아이디 입니다."})
    nick = models.CharField(max_length=20, unique=True, default=None, error_messages={'unique' : "이미 존재하는 닉네임 입니다."})
    name = models.CharField(max_length=20,)
    password = models.CharField(max_length=20, )


    def __str__(self):
        return self.user_id
    


# class AuthUser(AbstractUser):
#     class Meta: