from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'recipes/home.html', context={
        'name' : 'Ramon Algaranhar Pereira',
    })


def sobre(request):
    return HttpResponse('SOBRE RECIPES')

def contato(request):
    return HttpResponse('CONTATO RECIPES')
