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
    img_location = models.ForeignKey(Location, default=1)
    img_category = models.ForeignKey(Category, default=1)
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

