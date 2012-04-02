from trajan.plugins.blog.models import Post

def posts(request):
	context = {'recent_posts' = Post.objects.published()[:5]}
	return context
	
def tags(request):
	context = {'tags': Post.tags.all()}
	return context