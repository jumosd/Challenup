from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.


class Webtoon(models.Model):
    penname = models.CharField(max_length=20)
    title = models.CharField(max_length=20)
    genre = models.CharField(max_length=20)
    tag = models.CharField(max_length=20)
    thumbnail = models.ImageField()



class Category(models.Model):
    #판타지
    fantasy = models.CharField(max_length=20, )
    #현대물
    modern = models.CharField(max_length=20, )
    #로맨스
    romance = models.CharField(max_length=20, )
    #무협/사극
    martial_arts  = models.CharField(max_length=20, )
    #일상/개그
    daily = models.CharField(max_length=20, )
    #스릴러
    thriller = models.CharField(max_length=20, )
    #스릴러
    sports = models.CharField(max_length=20, )




# work = Category.objects.creat(Fantasy = "혁의 소설")
# work2 = Category.objects.create(genre6 = "깜피의만화")
# work3 = Category.objects.create(genre4 = "진수의 소설")
# work4 = Category.objects.create(genre7 = "나의의19금")
