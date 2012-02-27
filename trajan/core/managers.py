from django.db.models import Manager

class PageManager(Manager):
    
    def published(self):
        return self.model.objects.filter(published=True)