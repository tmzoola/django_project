from django.db import models

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    time_created = models.DateTimeField(auto_now_add=True)
    time_updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    
    
    def __str__(self) -> str:
        return self.name
    
    class Meta:
        ordering = ['-name']
        
        
from django.db import models

class Actor(models.Model):
    actor_name = models.CharField(max_length=255)
    about = models.TextField()
    age = models.CharField(max_length=3)
    time_created = models.DateTimeField(auto_now_add=True)
    time_updated = models.DateTimeField(auto_now=True)
    is_acting = models.BooleanField(default=True)

    def __str__(self):
        return self.actor_name
