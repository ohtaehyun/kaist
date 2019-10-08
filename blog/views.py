from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def post_list(request):
    msg = "AAAAAAAAAAAAAAAAAAAAA"
    return HttpResponse("<h1>asdasdasdas</h1>"+msg)


def mysum(request,a,b):
    return HttpResponse("<h1>"+str(a+b)+"</h1>")



