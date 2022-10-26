from multiprocessing import context
from unicodedata import category
from django.shortcuts import render

from allnews.models import news, news_second
# from matplotlib.widgets import Slider
from .models import *
from category.models import category, subcategory
# Create your views here.

def home(request):
    cat = category.objects.all()
    subcat = subcategory.objects.all()
    # print(cat)
    data = slider.objects.all()
    data1 = news.objects.filter(News_category__category_name = 'Trending')
    data2 = news.objects.filter(News_category__category_name='Business')
    data3 = news.objects.filter(News_category__category_name='Urban')
    data4 = news.objects.filter(News_category__category_name='sport')
    data5 = news.objects.filter(News_category__category_name='Tech')
    data6 = news.objects.filter(News_category__category_name='Lifestyle')
    data7 = news.objects.filter(News_category__category_name='Lifestyle')
    data8 = news_second.objects.all()
    data9 = gallery.objects.all()
    data10 = popular.objects.all()
    data11 = features.objects.all()
    context = {'cat':cat ,'data': data , 'data1':data1 , 'data2':data2, 'data3':data3, 'data4':data4, 'data5':data5, 'data6':data6, 'data7':data7, 'data8':data8, 'data9':data9, 'data10':data10, 'data11':data11,'cat':cat}
    return render(request,"index.html" , context)
    
def newsdetail(request):
    news_id = request.GET.get('id')
    
    data = news.objects.filter(id=news_id).values()
    print(data)
    return render(request, 'newsdetail.html',{'data':data})

