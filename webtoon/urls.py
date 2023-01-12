from django.urls import path
from . import views

app_name = "webtoon"

urlpatterns = [
    path('', views.webtoon_main, name="webtoonmain"),
    path('detail/', views.webtoon_detail, name="webtoondetail"),
    path('detail/<int:id>', views.webtoon_detail, name="webtoondetail"),
    path('create/', views.webtoon_create, name="webtooncreate"),
    path('update/', views.webtoon_update, name="webtoonupdate"),
    path('delete/', views.webtoon_delete, name="webtoondelete"),
    
]