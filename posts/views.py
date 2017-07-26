from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post
from django.shortcuts import get_object_or_404
from .forms import PostForm
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# def post_create(request): #what will be contain when i open 127.0.0.1:8000/home   check the urls tab
# 	post_list = Post.objects.all() #check line 13 we call all the object and add it in the html create file
# 	post_filter = Post.objects.filter(title__contains = 't')
# 	allvalue = Post.objects.get(id=5)
# 	context = {
	
# 		'title': 'post page', #check the create templets
# 		'content': 'you change my life',
# 		'user': request.user,
# 		'list': post_list,
# 		'filter':post_filter,
# 		'allval': allvalue,


# 	}

# 	return render (request, 'create.html', context)

def post_list(request):
	obj_list = Post.objects.all() #.order_by('-timestamp', 'title') to order for certine html
	paginator = Paginator(obj_list, 8) # Show 5 contacts per page

	page = request.GET.get('page')
	try:
		objs = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		objs = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		objs = paginator.page(paginator.num_pages)

	context = {

	"post_list": objs,
	}
	return render(request, "post_list.html", context)

def post_detail(request, post_id):
	# obj = get_object_or_404(Post, id=post_id)
	obj = Post.objects.get(id=post_id)
	context = {
		'instance': obj,

	}
	return render(request, 'post_detail.html', context)

# def	post_update(request):
# 	return render (request, 'update.html', {})

def	post_delete(request):
	return render (request, 'delete.html', {})

# def	post_list(request):
# 	return render (request, 'list.html', {})

# def	post_detail(request):
# 	return render (request, 'detail.html', {})



# def post_anythimg (request):
# 	return rendur (request, anything.html, {}) to create html file

def post_create(request):
	form = PostForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		form.save()
		messages.success(request, "Created")
		return redirect('posts:list')
	context = {
		'form':form,

	}
	return render(request, 'post_create.html', context)


def post_update(request, post_id):
	post_object = get_object_or_404(Post, id=post_id)
	form = PostForm(request.POST or None, request.FILES or None, instance=post_object)
	if form.is_valid():
		form.save()
		messages.success(request, "Updated")
		return redirect('posts:list')
	context = {
		'form':form,
		'post_object':post_object,
	}
	return render(request, 'post_update.html', context)

def post_delete(request, post_id):
	Post.objects.get(id=post_id).delete()
	messages.warning(request, "Deleted")
	return redirect ('posts:list')