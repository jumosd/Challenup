from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse

# Create your models here.


class User(AbstractUser):

    nickname = models.CharField(max_length= 20, blank=True, )
    username = models.CharField(max_length=20, blank =True, unique=True)
    profile_photo = models.ImageField(blank=True)
    # 팔로워,팔로우들은 유저끼리 다대다 관계 "slef" 즉 유저 <-> 유저 간의 다대다 관계이다
    follower = models.ManyToManyField("self")   
    following = models.ManyToManyField("self")
    is_creater = models.BooleanField(blank=True, default=0)
    is_procreater = models.BooleanField(blank=True, default=0)

    # 이기능은 추정컨데 url경로로 키워드를 보내주는거같다 
    # def get_absolute_url(self):
    #     return reverse("users:detail", kwargs = {"username":self.username})
    
    def __str__(self):
        return self.nickname
    
    def get_username(self):
        return self.username




# class 프로크리에이터( 모델 하나더~ ):
#     회원 =  models.ForeignKey(회원)
#     글러 =  상태체크
#     그림러 = 상태체크
#     성우 = 상태체크

# class 아마추어( 모델 하나더~ ):
#     회원 =  models.ForeignKey(회원)
#     글러 =  상태체크
#     그림러 = 상태체크
#     성우 = 상태체크