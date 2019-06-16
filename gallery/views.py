from django.shortcuts import render
from .models import Image
# Create your views here.
def welcome(request):
    image = Image.objects.all()

    return render(request, 'index.html',{'image':image})

def show(request):
    image = Image.objects.all()
    return render(request, 'gallery.html',{'image':image}) 


def search_results(request):

    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_articles = Image.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"images": searched_articles})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})
