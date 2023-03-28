import os
from django.conf import settings
from django.http import HttpResponseForbidden
from django.shortcuts import render,redirect,get_object_or_404
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
        author = request.user
        title = request.POST['title']
        penname = request.POST['penname']
        description = request.POST['description']
        image = request.FILES['image']
        thumbnail = request.FILES['thumbnail']
        genre = request.POST['genre']
        tag = request.POST['tag'] 
        Webtoon.objects.create(author= author,title=title,penname=penname,description=description, image=image, thumbnail=thumbnail, genre=genre, tag=tag)
        return redirect('webtoon:webtoonmain')
    return render(request, 'create_webtoon.html')
     
@login_required
def webtoon_update(request,pk):
    webtoon = get_object_or_404(Webtoon, pk=pk)
    if request.method == 'POST':
        form = WebtoonForm(request.POST, request.FILES, instance=webtoon,)
        if form.is_valid():
            form.save()
            return redirect('webtoon:webtoondetail', pk=pk)
    else:  
        form = WebtoonForm(instance=webtoon)
    print("수정안되쥬??")
    context = {
        'form': form,
        'webtoon': webtoon,
    }
    return render(request, 'webtoon/update.html', context)

@login_required
def webtoon_delete(request, pk):
    webtoon = get_object_or_404(Webtoon, pk=pk)
    if request.user != webtoon.author and not request.user.is_staff:
        return HttpResponseForbidden("당신은 이 웹툰을 삭제할 권한이 없습니다.")
    if request.method == "POST":
        
        webtoonpath =os.path.join(settings.MEDIA_ROOT,webtoon.image.path)
        if os.path.exists(webtoonpath):
            os.remove(webtoonpath)
        thumbnailpath =os.path.join(settings.MEDIA_ROOT,webtoon.thumbnail.path)
        os.remove(thumbnailpath)
        webtoon.delete()
        return redirect(reverse("webtoon:webtoonmain"))
    else:
        return redirect(reverse("webtoon:webtoondetail", kwargs={"pk": pk}))
    