from django.http import HttpResponse
from django.shortcuts import render

from .models import Item


# Create your views here.
def index(request):
    items = Item.objects.all()

    return HttpResponse(items)


def item(request):
    return HttpResponse("Hello, world. You're at the food item page.")
