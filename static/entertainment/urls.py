
from django.urls import path,include
from entertainment import views


urlpatterns = [
    path('entertainment/',views.entertainment,name='entertainment'),
  

]
