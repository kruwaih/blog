from django.shortcuts import render
from django.http import HttpResponse
from.models import Post

def post_create(request): #what will be contain when i open 127.0.0.1:8000/home   check the urls tab
	post_list = Post.objects.all() #check line 13 we call all the object and add it in the html create file
	post_filter = Post.objects.filter(title__contains = 't')
	allvalue = Post.objects.get(id=5)
	context = {
	
		'title': 'post page', #check the create templets
		'content': 'you change my life',
		'user': request.user,
		'list': post_list,
		'filter':post_filter,
		'allval': allvalue,


	}
	return render (request, 'create.html', context)


def	post_update(request):
	return render (request, 'update.html', {})

def	post_delete(request):
	return render (request, 'delete.html', {})

def	post_list(request):
	return render (request, 'list.html', {})

def	post_detail(request):
	return render (request, 'detail.html', {})



# def post_anythimg (request):
# 	return rendur (request, anything.html, {}) to create html file