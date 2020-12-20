from django.http  import HttpResponse
from django.shortcuts import render,redirect
import datetime as dt
from django.http  import HttpResponse,Http404
from .models import *

def home(request):
    gallery = Image.objects.all()
    location = Location.objects.all()
    category = Categories.objects.all()

    if 'location' in request.GET and request.GET['location']:
        place = request.GET.get('location')
        gallery = Image.view_location(name)

    elif 'category' in request.GET and request.GET['category']:
        caty = request.GET.get('categories')
        gallery = Image.view_category(caty)
        return render(request, 'all-images.html', {"name":name,"images":images,"cat":cat })

    return render(request,"all-images.html",{"images":images,"location":location,"category":category})

def search_results(request):

    if 'category' in request.GET and request.GET["category"]:
        search_term = request.GET.get("category")
        searched_categories = Image.search_by_title(search_images)
        message = f"{search_images}"

        return render(request, 'search.html',{"message":message,"category": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})


