from django.db import models

# Create your models here.


class Image(models.Model):
    img_name = models.CharField(max_length = 255)
    description = models.TextField()
    
    def __str__(self) -> str:
        return self.description
    

class About(models.Model):
    title = models.CharField(max_length = 255)
    description = models.TextField()
    time_created = models.DateTimeField(auto_now_add=True, null = True)
    time_updated = models.DateTimeField(auto_now=True, null = True)
    
    
    
    def __str__(self) -> str:
        return self.title
    


class Student(models.Model):
    name = models.CharField(max_length = 255)
    description = models.TextField()
    time_created = models.DateTimeField(auto_now_add=True, null = True)
    time_updated = models.DateTimeField(auto_now=True, null = True)
    is_active = models.BooleanField(default = True)

