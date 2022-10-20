
from django.urls import path,include
from business import views


urlpatterns = [
    path('business/',views.business,name='business'),
  

]
