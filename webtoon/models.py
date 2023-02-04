from django.db import models
from django.core.exceptions import ValidationError
from account.models import User
# Create your models here.

#장고패턴임  생성되는 클래스마다 쓰는게아니라 이걸 상속받으면됨
class TimeStamedModel(models.Model):
    create_at = models.DateTimeField(auto_now_add=True)
    update_ap = models.DateTimeField(auto_now_add=True)
    # 아래의 옵션을 추가하면 타임스탬프모델은 테이블에 추가되지않음. 
    class Meta:
        abstract = True

class Webtoon(TimeStamedModel):
    author = models.ForeignKey(User,null=True, on_delete=models.CASCADE, related_name = "webtoon_author")
    penname = models.CharField(max_length=20)
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=500)
    image = models.ImageField(blank=True)
    thumbnail = models.ImageField()
    webtoon_like = models.ManyToManyField(User, related_name= "webtoon_like")

class Comment(TimeStamedModel):
    author = models.ForeignKey(
        User,
        null=True,
        on_delete=models.CASCADE,
        related_name = "comment_author")
    webtoon = models.ForeignKey(
        Webtoon,
        on_delete=models.CASCADE,
        related_name="comment_webtoon")
    comment = models.TextField(max_length=1000, blank=True)
    

# 댓글노출여부 - 댓글기능후제작
# 웹툰소개글 -
# 상태
# 태그
# 독점여부
# 웹툰장르
# 웹툰표지(썸네일)
# 웹툰
# 날짜
# 추천
# 비추천
# 구독버튼

