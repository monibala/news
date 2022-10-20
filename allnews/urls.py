
from django.urls import path,include
from allnews import views


urlpatterns = [
    path('business/',views.business_type,name='business'),
    path('entertainment/',views.entertainment,name='entertainment'),
    path('food/',views.foods,name='food'),
    path('lifestyle/',views.lifestyle,name='lifestyle'),
    path('pet/',views.pet,name='pet'),
    path('sport/',views.sport,name='sport'),
    path('tech/',views.tech,name='tech'),
    path('travel/',views.travel,name='travel'),
    path('urban/',views.urban,name='urban'),
    path('salads/', views.salads, name='salads'),
    path('markets/', views.markets, name='markets'),
    path('stock/', views.stock, name='stock'),
    path('hipster/', views.hipster, name='hipster'),
    path('businessdetail/', views.businessdetail, name='businessdetail'),
    path('entertaindetail/', views.entertaindetail, name='entertaindetail'),
    path('techdetail/', views.techdetail, name='techdetail'),
    path('fooddetail/', views.fooddetail, name='fooddetail'),
    path('sportdetail/', views.sportdetail, name='sportdetail'),
    path('catnews/', views.catnews, name='catnews'),
    path('asia/', views.asia, name='asia'),
    path('vlogging/', views.vlogging, name='vlogging'),   
    path('catdetail/',views.catdetail,name='catdetail'),
    path('subcat/',views.subcat,name='subcat'),
]
