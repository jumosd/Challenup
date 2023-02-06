from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'account'

urlpatterns =[
    # path('', auth_views.LoginView.as_view(), name='login'),
    path('', views.login_view, name="login"),
    path('signup/', views.signup_view, name="signup"),
    path('logout/', views.log_out, name="logout"),
]