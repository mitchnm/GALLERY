from django.db import models

# Create your models here.
class Location(models.Model):
    location = models.CharField(max_length=35, unique=True)

    def __str__(self):
        return self.location 

    def save_location(self):
        self.save()

class Category(models.Model):
    category = models.CharField(max_length=35, unique=True)

    def __str__(self):
        return self.category

    def save_category(self):
        self.save()

class Image(models.Model): 
    img_name = models.CharField(max_length=35)
    img_decription = models.TextField()
    # img_location = models.ForeignKey(Location, on_delete=models.CASCADE)
    # img_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    article_image = models.ImageField(upload_to = 'gallery/')

    def __str__(self):
        return self.img_name
    
    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()
    
    @classmethod
    def search_by_title(cls,search_term):
        photo = cls.objects.filter(img_name__icontains=search_term)
        return photo

    @classmethod
    def filter_by_location(cls,location):
        location_search = cls.objects.filter(img_location__location__icontains=location)
        return location_search

    @classmethod
    def filter_by_category(cls,category):
        category_search = cls.objects.filter(img_location__category__icontains=category)
        return category_search