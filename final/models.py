from django.db import models

# Create your models here.
class Image(models.Model):
    image = models.ImageField(blank=True, upload_to="images")
    image_name = models.CharField(max_length=200)
    image_description = models.TextField(max_length=600)
    image_link = models.CharField(max_length=200, blank=True)
    
    def __str__(self):
        return self.image_name
    
class Location(models.Model):
    location = models.CharField(Image, max_length=200)
    
    def __str__(self):
        return self.location
    
class Category(models.Model):
    category = models.CharField(Image, max_length=200)

    def __str__(self):
        return self.category
    