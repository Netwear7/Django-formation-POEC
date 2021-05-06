from django.shortcuts import render
# from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.template import loader
from .models import Recette


# Create your views here.
def index(request):
    template = loader.get_template('recette/index.html')
    context = {'name': 'Recette'}
    # return HttpResponse(template.render(context, request))
    return render(request, 'recette/index.html', context)


# Page Menu
def menu(request):
    recettes = Recette.objects.all()
    context = {'name': 'Plat', 'recettes': recettes}
    return render(request, 'recette/menu.html', context)
