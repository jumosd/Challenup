from django.shortcuts import render
from .models import User

# Create your views here.


def login_view(request):

    return render(request, 'login/index.html')

def signup_view(request):

    if request.method == "POST":
            if request.POST['user_password'] == request.POST['user_password2']: 
                user = request.POST
                User.objects.create(
                    user_id=user['user_id'],
                    user_name=user['user_name'],
                    user_password=user['user_password'],)
                
                return render(request, 'home.html')
            
        
    
    else:
        return render (request, "signup/index.html")