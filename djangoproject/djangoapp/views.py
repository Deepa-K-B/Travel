from django.shortcuts import render
from .models import  Travelplace
from .models import  Team


# Create your views here.
from django.http import HttpResponse
def demo(request):
    obj=Travelplace.objects.all() #for fetching
    obj1 = Team.objects.all()
    return render(request,"index.html",{'result':obj,'res1':obj1})

#def about(request):
 #   return render(request,"about.html")