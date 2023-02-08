from django.shortcuts import render
from .forms import WebtoonForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def webtoon_main(request):
    return render(request, 'webtoon/main.html')

def webtoon_menu(request):
    return render(request, 'webtoon/menu.html')

def webtoon_detail(request):
    return render(request, 'webtoon/detail.html')

@login_required
def webtoon_create(request):
    if request.method == "GET":
        form = WebtoonForm()
        context = {
            'form': form
        }
        return render(request,'webtoon/create.html', context)
    else:
        return render(request, "webtoon/main.html")

def webtoon_update(request):
    if request.method == "POST":
        pass
    else:
        pass

def webtoon_delete(request):
    if request.method == "POST":
        pass
    else:
        pass