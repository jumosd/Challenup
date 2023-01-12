from django.urls import path
from . import views

app_name = 'acount'

urlpatterns =[
    path('', views.login_view, name="login"),
    path('signup/', views.signup_view, name="signup"),

]