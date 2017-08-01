from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post
from django.shortcuts import get_object_or_404
from .forms import PostForm
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from urllib.parse import quote
from django.http import Http404
from django.utils import timezone
from django.db.models import Q

def post_list(request):
    today = timezone.now().date()
    
    if request.user.is_staff or request.user.is_superuser:
        obj_list = Post.objects.all()
    else:
        obj_list = Post.objects.filter(draft=False).filter(publish__lte=today) #.order_by('-timestamp', 'title') to order for certine html
                                                                            # lte = less than equal
    query = request.GET.get("q")
    if query:
        obj_list = obj_list.filter(
            Q(title__icontains=query)|
            Q(content__icontains=query)|
            Q(author__first_name__icontains=query)|
            Q(author__last_name__icontains=query)
            ).distinct()


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
    "today":today,

    }
    return render(request, "post_list.html", context)

def post_detail(request, slug):
    obj = get_object_or_404(Post, slug=slug)
    # obj = Post.objects.get(slug=slug)
    if obj.publish >timezone.now().date() or obj.draft:
        if not (request.user.is_staff or request.user.is_superuser):
            raise Http404

    context = {
        'instance': obj,

    }
    return render(request, 'post_detail.html', context)

# def   post_update(request):
#   return render (request, 'update.html', {})

def post_delete(request):
    return render (request, 'delete.html', {})

# def   post_list(request):
#   return render (request, 'list.html', {})

# def   post_detail(request):
#   return render (request, 'detail.html', {})



# def post_anythimg (request):
#   return rendur (request, anything.html, {}) to create html file

def post_create(request):
    if not (request.user.is_staff or request.user.is_superuser):
        raise Http404
    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        obj = form.save(commit = False)
        obj.author = request.user
        obj.save()
        messages.success(request, "Created")
        return redirect('posts:list')
    context = {
        'form':form,

    }
    return render(request, 'post_create.html', context)


def post_update(request, slug):
    if not (request.user.is_staff or request.user.is_superuser):
        raise Http404
    post_object = get_object_or_404(Post, slug=slug)
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

def post_delete(request, slug):
    if not (equest.user.is_superuser):
        raise Http404
    Post.objects.get(slug=slug).delete()
    messages.warning(request, "Deleted")
    return redirect ('posts:list')