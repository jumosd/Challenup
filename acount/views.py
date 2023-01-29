from django.shortcuts import render,redirect
from .models import User
from .forms import UserForm
# Create your views here.


def login_view(request):
    if request.method == 'POST' :
        pass
    
    else:

        return render(request, 'login/index.html')

def signup_view(request):
    if request.method == "POST":
        signup_form = UserForm(request.POST)
        if signup_form.is_valid():
            User.objects.create
            return redirect('home')
    
    else:
        signup_form = UserForm()
        return render (request, "signup/index.html", {'signup_form': signup_form})