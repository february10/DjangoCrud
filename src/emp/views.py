from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def app_create(request):
    return HttpResponse("<h2> create </h2>")


def app_detail(request): 
    return HttpResponse("<h2> detail </h2>")


def app_update(request):
    return HttpResponse("<h2> update </h2>")


def app_delete(request):
    return HttpResponse("<h2> delete </h2>")

def app_list(request):
    return render(request, "index.html", {})
    #return HttpResponse("<h2> list </h2>")
