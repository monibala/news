
from django.urls import path,include
from allnews import views


urlpatterns = [
    path('business/',views.business,name='business'),
    path('entertainment/',views.entertainment,name='entertainment'),
    path('food/',views.food,name='food'),
    path('lifestyle/',views.lifestyle,name='lifestyle'),
    path('pet/',views.pet,name='pet'),
    path('sport/',views.sport,name='sport'),
    path('tech/',views.tech,name='tech'),
    path('travel/',views.travel,name='travel'),
    path('urban/',views.urban,name='urban'),

]
