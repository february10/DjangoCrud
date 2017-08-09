from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def app_crud(request):
    return HttpResponse("<h2> Hello there </h2>")
