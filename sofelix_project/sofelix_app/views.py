from django.shortcuts import render

# Create your views here.
from django.http import HttpRequest, HttpResponse


def index(request: HttpRequest) -> HttpResponse:
    return HttpResponse("¡Hola, mundo Sofelix!")