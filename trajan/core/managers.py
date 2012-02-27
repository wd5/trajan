from django.db.models import Manager

class PagesManager(Manager):
    
    def published(self):
        return self.model.objects.filter(published=True)