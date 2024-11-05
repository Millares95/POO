from django.http import HttpResponse

def index(request):
    return HttpResponse("Esta es la raíz de mi_ap.")

from django.shortcuts import render
from .models import SuperHeroes

def rojo(request):

    heroes_rojos = SuperHeroes.objects.filter(color="rojo")
    context = {'heroes_rojos': heroes_rojos}
    return render(request, 'mi_ap/rojo.html', context)
