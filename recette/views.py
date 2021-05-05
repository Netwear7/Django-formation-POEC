from django.shortcuts import render
# from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.template import loader


# Create your views here.
def index(request):
    template = loader.get_template('recette/index.html')
    context = {'name': 'Recette'}
    # return HttpResponse(template.render(context, request))
    return render(request, 'recette/index.html', context)


# Page Plat
def plat(request):
    context = {'name': 'Plat'}
    return render(request, 'recette/plat.html', context)
