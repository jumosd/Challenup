from django.shortcuts import render

# Create your views here.
def webtoon_main(request):
    return render(request, 'webtoon/main.html')

def webtoon_menu(request):
    return render(request, 'webtoon/menu.html')

def webtoon_detail(request):
    return render(request, 'webtoon/detail.html')

def webtoon_create(request):
    if request.method == "POST":
        pass
    else:
        pass
        return render(request, "webtoon/create.html")

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