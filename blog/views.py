# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from blog.models import Post
import random

def index(request):
	context = RequestContext(request)





	context_dict = {}
	post_list = Post.objects.order_by('-date')
	context_dict['posts'] = post_list



	return render_to_response('blog/index.html', context_dict, context)

def story(request, pk):
	context = RequestContext(request)

	#post_title = post_title_url.replace("_", " ")
	#post = get_object_or_404(Post, title=post_title)
	post = get_object_or_404(Post, pk=int(pk))
	story = post.story
	title = post.title
	context_dict = {}
	context_dict['title'] = title
	context_dict['story'] = story



	return render_to_response('blog/story.html', context_dict, context)

def stories(request):
	context = RequestContext(request)

	context_dict = {}
	post_list = Post.objects.order_by('-date')
	context_dict['posts'] = post_list

	return render_to_response('blog/stories.html', context_dict, context)	





