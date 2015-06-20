from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render_to_response
from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf
from django.core.paginator import Paginator, InvalidPage, EmptyPage, PageNotAnInteger
from django.forms import ModelForm
from mwalkerphotos.settings import MEDIA_URL
from models import Album, Tag, Image
import random





# Create your views here.
'''
def home(request):
    albums = Album.objects.all()
    
    images = []
    
    for album in albums.object_list:
        album.images = album.image_set.all()[:4]
    
    for img in album.images:
        images.append(img)
    
    image_to_display=random.sample(images, 6)
    
    
    
    context = {}
    template = "home.html"
    return render_to_response("home.html", dict(image_to_display=image_to_display, user=request.user, media_url=MEDIA_URL))
'''


def home(request):
 #   images = Image.objects.all()
    album = Album.objects.get(title='PHCC2015')
    images = album.image_set.all()
    random_img=random.sample(images, 9)
    ran1=random_img[0]
    ran2=random_img[1]
    ran3=random_img[2]
    ran4=random_img[3]
    ran5=random_img[4]
    ran6=random_img[5]
    ran7=random_img[6]
    ran8=random_img[7]
    ran9=random_img[8]
    return render_to_response("home.html", dict(ran1=ran1, ran2=ran2, ran3=ran3, ran4=ran4, ran5=ran5, ran6=ran6, ran7=ran7, ran8=ran8, ran9=ran9, media_url=MEDIA_URL))



def home2(request):
    """Main listing."""
    albums = Album.objects.all()
    if not request.user.is_authenticated():
        albums = albums.filter(public=True)

    paginator = Paginator(albums, 10)
    try: page = int(request.GET.get("page", '1'))
    except ValueError: page = 1

    try:
        albums = paginator.page(page)
    except (InvalidPage, EmptyPage):
        albums = paginator.page(paginator.num_pages)

#    random_img=random.sample(images, 6) 
#    print images

    return render_to_response("home.html", dict(random_img=random_img, user=request.user,
        media_url=MEDIA_URL))



def albums(request):
    """Main listing."""
    albums = Album.objects.all()
    if not request.user.is_authenticated():
        albums = albums.filter(public=True)

    paginator = Paginator(albums, 10)
    try: page = int(request.GET.get("page", '1'))
    except ValueError: page = 1

    try:
        albums = paginator.page(page)
    except (InvalidPage, EmptyPage):
        albums = paginator.page(paginator.num_pages)

    for album in albums.object_list:
        album.images = album.image_set.all()

    return render_to_response("list.html", dict(albums=albums, user=request.user,
        media_url=MEDIA_URL))

    
def album_view(request, title):
    """Album listing."""
    album = Album.objects.get(title=title)
    if not album.public and not request.user.is_authenticated():
        return HttpResponse("Error: you need to be logged in to view this album.")


    images = album.image_set.all()
    paginator = Paginator(images, 300)
   # try: page = int(request.GET.get("page", '1'))
   # except ValueError: page = 1#
   #
   # try:
   #     images = paginator.page(page)
   # except (InvalidPage, EmptyPage):
   #     images = paginator.page(paginator.num_pages)
   
    page = request.GET.get('page')
    try:
        images = paginator.page(page)
    except PageNotAnInteger:
        images = paginator.page(1)
    except EmptyPage:
         images = paginator.page(paginator.num_pages)
   
    return render_to_response("gallery.html", dict(album=album, images=images, user=request.user,
       media_url=MEDIA_URL))
    
#def album_view(request, title):
    
#    album=Album.objects.get(title=title)
#    images = album.image_set.all()
#    paginator = Paginator(images, 30)
#    album_url = "http://mwalker.photos/albums/%s" %(title)
    
#    template = "album.html"
    
#    return render_to_response("album.html", dict(album=album, images=images, media_url=MEDIA_URL))
    
    
