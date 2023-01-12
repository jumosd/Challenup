from django.shortcuts import render

# Create your views here.
def webtoon_main(request):
    
    return render(request, 'webtoon/main.html')

def webtoon_detail(request):
    return render(request, 'webtoon/detail.html')


def webtoon_create(request):
    
    return render(request, "webtoon/create.html")

def webtoon_update(request):
    pass

def webtoon_delete(request):
    pass