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

    MAINGENRE_CHOICES = {
	"MO": {"KOR_NAME": "현대물", "SUB_CAT_ID": 1},
	"AF": {"KOR_NAME": "로맨스", "SUB_CAT_ID": 2},
	"FA": {"KOR_NAME": "판타지", "SUB_CAT_ID": 3},
	"MA": {"KOR_NAME": "무협/사극", "SUB_CAT_ID": 4},
	"GA": {"KOR_NAME": "일상/개그", "SUB_CAT_ID": 5},
	"AC": {"KOR_NAME": "스릴러/액션", "SUB_CAT_ID": 6},	
    }
    SUB_CAT_1 = {
        "현대물":{
            "tag":[
                   "판타지","BL","빙의","피폐/시리어스","(포스트)아포칼립스)","시대물","GL","회귀",
                   "추리/미스테리","서바이벌/먼치킨","SF","HL","환생","공포/호러","스릴러/액션","일상/개그",
                   "단편","이종족","해피엔딩","요리/스포츠","원작","장편","신분차이","새드엔딩",
                   ]}}
    SUB_CAT_2 = {
        "로맨스":{
            "tag":[
                "현대","BL","빙의","피폐/시리어스","(포스트)아포칼립스)","판타지","GL","회귀","추리/미스테리",
                "서바이벌/먼치킨","시대물","HL","환생","공포/호러","스릴러/액션","SF","단편","이종족",
                "해피엔딩","요리/스포츠","원작","장편","신분차이","새드엔딩","일상/개그",
            ]
        }
        }
    
    SUB_CAT_3 = {
        "판타지":{
            "tag":["판타지","BL","빙의","피폐/시리어스","(포스트)아포칼립스)","시대물","GL","회귀",
                   "추리/미스테리","서바이벌/먼치킨","SF","HL","환생","공포/호러","스릴러/액션","일상/개그",
                   "단편","이종족","해피엔딩","요리/스포츠","원작","장편","신분차이","새드엔딩",]
        }
        }
    SUB_CAT_4 = {
        "무협/사극":{
            "tag":["판타지","BL","빙의","피폐/시리어스","(포스트)아포칼립스)","시대물","GL","회귀",
                   "추리/미스테리","서바이벌/먼치킨","SF","HL","환생","공포/호러","스릴러/액션","일상/개그",
                   "단편","이종족","해피엔딩","요리/스포츠","원작","장편","신분차이","새드엔딩",]
        }
        }
    SUB_CAT_5 = {
        "일상/개그":{
            "tag":["판타지","BL","빙의","피폐/시리어스","(포스트)아포칼립스)","시대물","GL","회귀",
                   "추리/미스테리","서바이벌/먼치킨","SF","HL","환생","공포/호러","스릴러/액션","일상/개그",
                   "단편","이종족","해피엔딩","요리/스포츠","원작","장편","신분차이","새드엔딩",]
        }
        }
    SUB_CAT_6 = {
        "스릴러/액션":{
            "tag":["판타지","BL","빙의","피폐/시리어스","(포스트)아포칼립스)","시대물","GL","회귀",
                   "추리/미스테리","서바이벌/먼치킨","SF","HL","환생","공포/호러","스릴러/액션","일상/개그",
                   "단편","이종족","해피엔딩","요리/스포츠","원작","장편","신분차이","새드엔딩",]
        }
        }
  


    # def find_sub_cat(id: int)-> dict:
    #     for v in MAINGENRE_CHOICE:
    #         if v["SUB_CAT_ID"] == id:
    #             return v["SUB_CAT_ID"]


    author = models.ForeignKey(User,null=True, on_delete=models.CASCADE, related_name = "webtoon_author")
    penname = models.CharField(max_length=20)
    title = models.CharField(max_length=40)
    description = models.CharField(max_length=500)
    image = models.ImageField(blank=True)
    thumbnail = models.ImageField(blank=True)
    webtoon_like = models.ManyToManyField(User, related_name= "webtoon_like")
    genre = models.CharField(max_length=20,choices=MAINGENRE_CHOICES, unique=True, blank=True)
    tag = models.CharField(max_length=20, unique=True, blank=True)
    
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

class Category(models.Model):
    parent = models.ForeignKey('self', related_name='children', on_delete=models.CASCADE, blank = 
    True, null=True)
    title = models.CharField(max_length=100) 
    slug = AutoSlugField(populate_from='title', unique=True, null=False, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        #enforcing that there can not be two categories under a parent with same slug
        
        # __str__ method elaborated later in post.  use __unicode__ in place of

        unique_together = ('slug', 'parent',)    
        verbose_name_plural = "categories"     

    def __str__(self):                           
        full_path = [self.title]                  
        k = self.parent
        while k is not None:
            full_path.append(k.title)
            k = k.parent
        return ' -> '.join(full_path[::-1])  


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

# 웹툰 생성일을 기준으로 조회수가장많은거 정렬 주에는