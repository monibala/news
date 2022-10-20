
from django.urls import path,include
from aboutus import views


urlpatterns = [
    path('about/',views.about,name='about'),
]
