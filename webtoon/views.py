from django.shortcuts import render,redirect
from django.urls import reverse
from .forms import WebtoonForm
from django.contrib.auth.decorators import login_required
from . models import Webtoon

# Create your views here.
def webtoon_main(request):
    webtoons = Webtoon.objects.all().order_by('-id')
    context ={
        "webtoons" : webtoons
    }
    return render(request, 'webtoon/main.html', context)

def webtoon_menu(request):
    return render(request, 'webtoon/menu.html')

def webtoon_detail(request, pk):
    try:
        webtoon = Webtoon.objects.get(pk = pk)
        context = {"webtoon": webtoon}
        return render(request, "webtoon/detail.html", context)
    except Webtoon.DoesNotExist: # 👈 존재하지 않는 pk로 접근할 경우,
         return redirect(reverse("home"))

@login_required
def webtoon_create(request):
    if request.method == "GET":
        form = WebtoonForm()
        print (request.user)
        context = {
            'form': form
        }
        return render(request,'webtoon/create.html', context)
    elif request.method == 'POST':
        form = WebtoonForm(request.POST, request.FILES)
        
        webtoon = form.save

        author = request.user
        title = request.POST['title']
        penname = request.POST['penname']
        description = request.POST['description']
        image = request.FILES['image']
        thumbnail = request.FILES['thumbnail']
        genre = request.POST['genre']
        tag = request.POST 

        Webtoon.objects.create(author= author,title=title,penname=penname,description=description, image=image, thumbnail=thumbnail)
        return redirect('webtoon:webtoonmain')
    return render(request, 'create_webtoon.html')
    


    

def webtoon_update(request):
    if request.method == "POST":
        pass
    else:
        pass

def webtoon_delete(request):
    if request.method == "POST":

        
        # object = Webtoon.objects.get(pk=<object_id>)
        object.delete()
    





