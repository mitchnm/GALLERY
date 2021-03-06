from django.shortcuts import render
from .models import Image
# Create your views here.
def welcome(request):
    image = Image.objects.all()
    return render(request, 'index.html',{'image':image})

def show(request,id):
    image = Image.objects.filter(id=id)
    return render(request, 'gallery.html',{'image':image}) 


def search_results(request):
    # if 'image' in request.GET and request.GET["image"]:
    #     search_term = request.GET.get("image")
    #     print(search_term)
    #     searched_categories = Category.objects.filter(name=search_term)
    #     print(searched_image)
    #     photo=[]
    #     for category in searched_categories:
    #         category_id = category.id
    #         searched_images = Image.search_by_category(category_id)
    #         photo.extend(searched_images)
    if 'article' in request.GET and request.GET["article"]:
        search_term = request.GET.get("article")
        searched_articles = Category.search_by_category(search_term)
        message = f"{search_term}"
        return render(request, 'search.html',{"message":message,'images':searched_articles})
    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})

def get_category(request,category):
    category_results = Category.objects.all()
    category_result = Image.objects.filter(image_category__category =category)
    return render(request,'search.html',{'all_images':category_result,'category_results':category_results})

def get_location(request,location):
    location_results = Location.objects.all()
    location_result = Image.objects.filter(image_location__location=location)
    return render(request,'search.html',{'all_images':location_result,'location_results':location_results})