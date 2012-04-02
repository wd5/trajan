from django.shortcuts import get_object_or_404, redirect, render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from trajan.core.models import *
# Authentication stuff.  This is a handly decorator used to force a user to login.
from django.contrib.auth.decorators import login_required
import urllib
    
def render_page(request, page_slug):
    context = {}
    page = get_object_or_404(Page, slug=page_slug)
    context['content'] = page
    
    return render(request, 'core/page.html', context)
    
 