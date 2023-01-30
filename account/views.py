from django.shortcuts import render,redirect

# Create your views here.


def login_view(request):

    return render(request, 'login/index.html')

def signup_view(request):
    return render (request, "signup/index.html", )