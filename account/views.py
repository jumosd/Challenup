from django.shortcuts import render,redirect
from django.urls import reverse
from django.contrib.auth import logout
#로그인 함수형으로 구현
from django.contrib.auth import authenticate, login
from .forms import UserForm

def login_view(request):

    if request.method == 'GET':
        return render(request, 'login/index.html')
    
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect(reverse('home'))

        else: 
            # Return an 'invalid login' error message. 
            return render(request, 'login/index.html')


def signup_view(request):
    if request.method == 'GET':
        signup_form = UserForm()
        return render (request, "signup/index.html",{"signup_form" : signup_form} )


def log_out(request):
    logout(request)
    return redirect(reverse('home'))