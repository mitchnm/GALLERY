from django.shortcuts import render
from .models import Image
# Create your views here.
def welcome(request):
    image = Image.objects.all()
    return render(request, 'gallery.html',{'image':image})

