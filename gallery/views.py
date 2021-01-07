from django.http  import HttpResponse
from django.shortcuts import render,redirect
import datetime as dt
from django.http  import HttpResponse,Http404
from .models import *

def home(request):
    gallery = Image.objects.all()
    location = Location.objects.all()
    category = Category.objects.all()

    if 'location' in request.GET and request.GET['location']:
        place = request.GET.get('location')
        gallery = Image.view_location(place)

    elif 'category' in request.GET and request.GET['category']:
        caty = request.GET.get('category')
        gallery = Image.view_category(caty)
        return render(request, 'gallery.html', {"name":name,"gallery":gallery,"caty":caty })

    return render(request,"gallery.html",{"gallery":gallery,"location":location,"category":category})

def search_results(request):

    if 'category' in request.GET and request.GET["category"]:
        search_images = request.GET.get("category")
        searched_categories = Image.search_by_category(search_images)
        message = f"{search_images}"

        return render(request, 'search.html',{"message":message,"category": searched_categories})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})

def get_image_by_id(request,image_id):
    try:
        image = Image.objects.get(id = image_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"index.html", {"image":image})


