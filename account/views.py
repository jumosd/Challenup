from django.shortcuts import render,redirect
from django.urls import reverse
#로그인 함수형으로 구현
from django.contrib.auth import authenticate, login, models, logout
from .forms import UserForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm


def login_view(request):

    if request.method == 'GET':
        return render(request, 'login/index.html')
    
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        print(username,type(username))
        print(password,type(password))

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect(reverse('home'))

        else: 
            # Return an 'invalid login' error message. 
            return render(request, 'login/index.html')


# def signup_view(request):

#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             # 게시글 목록 페이지
#             return redirect('articles:index')
#     else:
#         form = UserCreationForm(UserForm)
#         context = {
#         'form': form
#         }
#     return render(request, 'signup/index.html', context)

#### 커스텀 유저모델##  여기다가 합쳐야됨

def signup_view(request):
    if request.method == 'GET':
        form = UserForm()
        return render (request, "signup/index.html",{"form" : form} )
    
    elif request.method == "POST":
        signup_form = UserForm(request.POST)
        if signup_form.is_valid():
            
            signup_form.save()

            username = signup_form.cleaned_data['username']
            password = signup_form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirect to a success page.
                return redirect(reverse('home'))


                # Return an 'invalid login' error message. 
        return render(request, 'login/index.html')
        


def log_out(request):
    logout(request)
    return redirect(reverse('home'))