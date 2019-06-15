from django.shortcuts import render
from .models import Image
# Create your views here.
def welcome(request):
    image = Image.objects.all()
    return render(request, 'base.html',{'image':image})

def show(request):
    return render(request, 'gallery.html') 


def search_results(request):

    if 'article' in request.GET and request.GET["article"]:
        search_term = request.GET.get("article")
        searched_articles = Article.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"articles": searched_articles})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})
