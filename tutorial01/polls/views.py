from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):                               # reques es un objeto tipo HttpRequest ?
    return HttpResponse("Hello, world. You're ar the polls index")


def about(request):
    return HttpResponse("soy una pagina de prueba")