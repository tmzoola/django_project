from django.urls import path
from . import views 


urlpatterns = [
    path('home/',views.home, name='home' ),
    path('index/',views.index, name='index'),
    path('student/<int:id>/',views.student, name='student'),
]
