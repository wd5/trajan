from django.db.models import Manager

class PostManager(Manager):
    def by_author(self, user):
        return self.model.objects.filter(user=user)
        
    def published(self):
        return self.model.objects.filter(published=True)
        
    def by_category(self, category_slug):
        return self.model.objects.filter(category__slug=category_slug)
