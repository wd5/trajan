from django import template
from trajan.plugins.blog.models import Post

register = template.Library()

@register.inclusion_tag('blog/templatetags/post_snippet.html')
def get_blog_posts(posts=3):
    context = {}
    context['posts'] = Post.objects.all()[:posts]
    return context
    
@register.inclusion_tag('blog/templatetags/tag_snippet.html')
def tag_widget():
	context = {'tags': Post.tags.all()}
	return context
	
	
@register.inclusion_tag('blog/templatetags/recent_posts.html')
def recent_post_widget(posts=3):
	context = {'posts': Post.objects.published()[:posts]}
	return context