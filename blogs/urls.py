
from django.urls import path,include
from blogs import views


urlpatterns = [
    path('blog/',views.blog,name='blog'),
  

]
