from django.shortcuts import render, get_object_or_404
from traveler.models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def trip(request, trip_slug):
    context = {}
    trip = get_object_or_404(Trip, slug=trip_slug, published=True)
    context['trip'] = trip
    
    return render(request, 'traveler/trip.html', context)

def trips(request):
    trips = Trip.objects.published()
    
    # Set up the paginator with how many objects you want to limit each page to.
    paginator = Paginator(trips, 4)
    # Get the page paramter to decide what page you want.  Default is set to the first page.
    page = request.GET.get('page', 1)
    try:
        context = {'trips': paginator.page(page)}
    except PageNotAnInteger:
        context = {'trip': paginator.page(1)}
    except EmptyPage:
        context = {'trips': paginator.page(paginator.num_pages)}
    '''
     Its important to note that when the view sends the blog_posts objects back you have to extract the actual objects
     using the object_list.  So to loop through blog posts in the template, it would be like this::
     
     {% for post in blog_posts.object_list %}
    
    '''
    return render(request, 'traveler/trips.html', context)