
from django.urls import path,include
from lifestyle import views


urlpatterns = [
    path('style/',views.style,name='style'),
  

]
