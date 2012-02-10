from django.shortcuts import render, get_object_or_404
from brew.models import Beer

def view_beer(request, beer_slug):
    context = {'beer': get_object_or_404(Beer, slug=beer_slug)}
    return render(request, 'brew/single_brew.html', context)

def beers(request):
    context = {'beers': Beer.objects.published()}
    return render(request, 'brew/beers.html', context)