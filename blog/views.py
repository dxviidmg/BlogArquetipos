from django.shortcuts import render,  get_object_or_404
from django.utils import timezone
from .models import Post

def post_list(request):
	template_name = 'blog/post_list.html'
	posts = Post.objects.filter(fecha_publicado__lte=timezone.now()).order_by('fecha_publicado')
	context = {
	'posts': posts
	}
	return render(request, template_name, context)