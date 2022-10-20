from django.shortcuts import render

# Create your views here.

def business(request):
    return render(request,"business.html")

def entertainment(request):
    return render(request,"entertainment.html")    

def food(request):
    return render(request,"food.html")   

def lifestyle(request):
    return render(request,"lifestyle.html")   

def pet(request):
    return render(request,"pet.html")   

def sport(request):
    return render(request,"sport.html")   

def tech(request):
    return render(request,"tech.html")   

def travel(request):
    return render(request,"travel.html")   

def urban(request):
    return render(request,"urban.html")                               
