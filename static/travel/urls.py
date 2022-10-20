
from django.urls import path,include
from travel import views


urlpatterns = [
    path('travel/',views.travel,name='travel'),
  

]
