from django.shortcuts import render

from home.models import news_trend
from .models import *

# Create your views here.

def business_type(request):
    
    data = news.objects.filter(News_category__category_name='Business')
    print(data)
    data1 = news_second.objects.all()
    context = {'data':data, 'data1':data1}
    return render(request,"business.html",context)

def entertainment(request):
   
    data = news.objects.filter(News_category__category_name='Entertainment')
    data1 = news_second.objects.all()
    context = {'data':data, 'data1':data1}
    return render(request,"entertainment.html",context)    

def foods(request):
    data = news.objects.filter(News_category__category_name='Food')
    data1 = news_second.objects.all()
    context = {'data':data, 'data1':data1}
    return render(request,"food.html",context)   

def lifestyle(request):
    data = news.objects.filter(News_category__category_name='Lifestyle')
    data1 = news_second.objects.all()
    context = {'data':data, 'data1':data1}
    return render(request,"lifestyle.html",context)   

def pet(request):
    data = news.objects.filter(News_category__category_name='pets')
    data1 = news_second.objects.all()
    context = {'data':data, 'data1':data1}
    return render(request,"pet.html",context)   

def sport(request):
    data = news.objects.filter(News_category__category_name='sport')
    data1 = news_second.objects.all()
    context = {'data':data, 'data1':data1}
    return render(request,"sport.html",context)   

def tech(request):
    data = news.objects.filter(News_category__category_name='Tech')
    data1 = news_second.objects.all()
    context = {'data':data, 'data1':data1}
    return render(request,"tech.html",context) 
    

def travel(request):
    data = news.objects.filter(News_category__category_name='Travel & Leisure')
    data1 = news_second.objects.all()
    context = {'data':data, 'data1':data1}
    return render(request,"travel.html",context)   

def urban(request):
    data = news.objects.filter(News_category__category_name='Urban')
    data1 = news_second.objects.all()
    context = {'data':data, 'data1':data1}
    return render(request,"urban.html",context)                               
def salads(request):
    return render(request, 'salads.html')
def markets(request):
    return render(request, 'markets.html')
def stock(request):
    return render(request, 'stock.html')
def hipster(request):
    return render(request, 'hipster.html')
def vlogging(request):
    return render(request, 'vlogging.html')
def businessdetail(request):
    business_id = request.GET.get('id')
    
    data = news.objects.filter(id=business_id)
    print(data)
    return render(request, 'businessdetail.html',{'data':data})
def entertaindetail(request):
    entertain_id = request.GET.get('id')
    
    data = news.objects.filter(id=entertain_id)
    print(data)
    return render(request, 'entertaindetail.html',{'data':data})

def techdetail(request):
    tech_id = request.GET.get('id')
    
    data = news.objects.filter(id=tech_id)
    print(data)
    return render(request, 'techdetail.html',{'data':data})

def fooddetail(request):
    food_id = request.GET.get('id')
    
    data = foods.objects.filter(id=food_id)
    print(data)
    return render(request, 'fooddetail.html',{'data':data})

def sportdetail(request):
    sport_id = request.GET.get('id')
    
    data = news.objects.filter(id=sport_id)
    print(data)
    return render(request, 'sportdetail.html',{'data':data})

def catnews(request):
    cat_id = request.GET.get('id')
    cat_data = category.objects.filter(category_name=cat_id).values()
    # sub_cat = subcategory.objects.filter(category_name=cat_data)
    print(cat_data)
    data = news.objects.filter(News_category__category_name=cat_id)
    print(data)
    return render(request, 'catnews.html',{'data':data, 'cat_data':cat_data})

def asia(request):
    return render(request, 'asia.html')
def catdetail(request):
    cat_id = request.GET.get('id')
    
    cat_data = category.objects.get(id=cat_id)
    sub_cat = subcategory.objects.filter(category_name=cat_data)
    print(sub_cat)
    data = news.objects.filter(News_category__category_name = cat_data)
    print(data)
    data1 = news_second.objects.all()
    context = {'cat_data':cat_data, 'sub_cat':sub_cat ,'data':data, 'data1':data1}
    return render(request, 'catdetail.html', context)
def subcat(request):
    cat_id = request.GET.get('id')
    cat = category.objects.filter(category_name=cat_id).values()
    subcat_data = subcategory.objects.get(subcategory_name=cat_id)
    print(subcat_data)
    
    data = news.objects.filter(News_subcategory__subcategory_name= subcat_data)
    print(data)
    context = { 'subcat_data':subcat_data ,'data':data}
    return render(request, 'subcat.html', context)
