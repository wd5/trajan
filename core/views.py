from django.shortcuts import get_object_or_404, redirect, render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic.simple import direct_to_template
# Import your models.
from blog.models import *
from core.models import *
# Authentication stuff.  This is a handly decorator used to force a user to login.
from django.contrib.auth.decorators import login_required
from brew.models import Beer
from locations.models import Location
from django.utils import simplejson
import urllib

def photos(request):
    page = request.GET.get('page', '1')
    if page == '1':
        num_photos = 0
    else:
        num_photos = 12 * int(page)
    fotochest_call = 'http://fotochest.com/api/v1/photo/?format=json&limit=12&offset=%s&username=dstegelman' % num_photos
    fotochest_feed = urllib.urlopen(fotochest_call)
    fotochest_json = fotochest_feed.read()
    photos = simplejson.loads(fotochest_json)
    next_page = int(page) + 1
    if page == '1':
        previous_page = "None"
    else:
        previous_page = int(page) - 1
    context = {}
    context['photos'] = photos
    context['next_page'] = next_page
    context['previous_page'] = previous_page
    return render(request, "core/photos.html", context)
    
def locations(request):
    context = {'locations': Location.objects.all()}
    return render(request, 'blog/locations.html', context)


def location(request, location_id):
    location = get_object_or_404(Location, pk=location_id)
    blog_posts = Post.objects.published().filter(location=location)
    statuses = Status.objects.filter(location=location)
    
    paginator = Paginator(blog_posts, 4)
    status_paginator = Paginator(statuses, 4)
    # Get the page paramter to decide what page you want.  Default is set to the first page.
    page = request.GET.get('page', 1)
    try:
        context = {'blog_posts': paginator.page(page)}
        context["statuses"] = status_paginator.page(page)
    except PageNotAnInteger:
        context = {'blog_posts': paginator.page(1)}
        context["statuses"] = status_paginator.page(1)
    except EmptyPage:
        context = {'blog_posts': paginator.page(paginator.num_pages)}
        context["statuses"] = status_paginator.page(status_paginator.num_pages)
    return render(request, 'blog/index.html', context)
    
    
def render_page(request, page_slug):
    context = {}
    page = get_object_or_404(Page, slug=page_slug)
    context['content'] = page
    
    return render(request, 'core/page.html', context)
    
    