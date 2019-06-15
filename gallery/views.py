from django.shortcuts import render
from .models import Image
# Create your views here.
def welcome(request):
    image = Image.objects.all()
    return render(request, 'base.html',{'image':image})

def show(request):
    return render(request, 'gallery.html') 