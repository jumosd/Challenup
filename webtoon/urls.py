from django.urls import path
from . import views

app_name = "webtoon"

urlpatterns = [
    path('', views.webtoon_main, name="webtoonmain"),
    path('menu/', views.webtoon_menu, name="webtoonmenu"),
    path('detail/<int:pk>/', views.webtoon_detail, name="webtoondetail"),
    path('create/', views.webtoon_create, name="webtooncreate"),
    path('update/<int:pk>', views.webtoon_update, name="webtoonupdate"),
    path('delete/<int:pk>', views.webtoon_delete, name="webtoondelete"),
]