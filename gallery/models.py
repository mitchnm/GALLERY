from django.db import models

# Create your models here.
class Image(models.Model): 
    img_name = models.CharField(max_length=35)
    img_decription = models.TextField()
    # img_location = models.ForeignKey(location)
    # img_category = models.ForeignKey(category)
    article_image = models.ImageField(upload_to = 'gallery/')

    def __str__(self):
        return self.img_name

class