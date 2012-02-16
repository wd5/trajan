from trajan.core.models import Page
def pages(request):
    context = {}
    pages = Page.objects.all()
    context['pages'] = pages
    return context
    