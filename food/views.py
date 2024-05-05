from django.http import HttpResponse
from django.shortcuts import render

from .models import Item


# Create your views here.
def index(request):
    items = Item.objects.all()

    return render(
        request,
        'index.html',
        {
            'items': items,
        }
    )


def detail(request, id):
    item = Item.objects.get(pk=id)

    return render(request, 'detail.html', {
        'item': item,
    })
