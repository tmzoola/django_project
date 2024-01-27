from django.shortcuts import render
from django.http import HttpResponse
from .models import Image,About, Student


# Create your views here.



def home(request):
    images = Image.objects.all()
    about = About.objects.get(pk=1)
    
    
    return render(request, "browny/index.html", context={"images":images, "about":about})


def index(request):
    students = Student.objects.all()
    
    return render(request, "browny/student.html", {"students":students})


def student(request, id):
    student = Student.objects.get(pk=id)
    
    return HttpResponse(f"This is student {student.description}")