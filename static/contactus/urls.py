
from django.urls import path,include
from contactus import views


urlpatterns = [
    path('contact/',views.contact,name='contact'),
]
