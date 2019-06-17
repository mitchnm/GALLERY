from django.test import TestCase
from .models import Location,Category,Image
# Create your tests here.



# REMEMEMBER TO QUERY ALL THE OBJECTS FROM THE DATABASE FOR TETSING EACH CLASS
#
# REMEMBER
# REMEMBER
class LocationTestClass(TestCase):
   #Set up method

   def setUp(self):
       self.nairobi = Location(location = 'Nairobi')

   #Testing insatnce

   def test_instance (self):
       self.assertTrue(isinstance(self.nairobi,Location))


   # Testing save method
   def test_save_method(self):
       self.nairobi.save_location()


class CategoryTestClass(TestCase):
   #Set up method

   def setUp(self):
       self.food = Category(category = 'Food')

   #Testing insatnce

   def test_instance (self):
       self.assertTrue(isinstance(self.food,Category))


   # Testing save method
   def test_save_method(self):
       self.food.save_category()

class ImageTestClass(TestCase):
       def setUp(self):
       #creating a new imaage
           self.new_image = Image(img_name ='eat',img_decription='eatingafrica', article_image='media/gallery/Fashion-3134828_1920.jpg', img_location='Nairobi', img_category='Sport')
       #Testing instance for the image

       def test_instance(self):
           self.assertTrue(isinstance(self.new_image,Image))

       # Testing the save method for the Image class
       def test_save_method(self):
           self.new_image.save_image()

       # Testing function to get image searched by category
       