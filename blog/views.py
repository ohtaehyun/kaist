from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def post_list(request):
    msg = "MESSAGE~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    return render(request,'post_list.html',{'msg':msg})


def mysum(request,a,b):
    return HttpResponse("<h1>"+str(a+b)+"</h1>")



