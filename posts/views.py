# from typing_extensions import Required
from django import forms
from django.http.response import HttpResponseBase, HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from .forms import PostForm
# Create your views here.


def index(request):
    # if the method is POST
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
    # If the form is valid
        if form.is_valid():
            #yes, save
            form.save()
          # Redirect to home
            return HttpResponseRedirect('/')

        else:
            # no, Show Error
            return HttpResponseRedirect(form.erros.as_json())

    # Get all posts, limit = 20
    posts = Post.objects.all().order_by('-created_at')[:20]

    # Show
    return render(request, 'posts.html', {'posts': posts})


def delete(request, post_id):
    # Find post
    post = Post.objects.get(id=post_id)
    post.delete()
    return HttpResponseRedirect('/')


def likes(request, post_id):
    post = Post.objects.get(id=post_id)
    post.like +=1
    post.save()
    return HttpResponseRedirect('/')

def edit(request, post_id):
    # if the method is POST
    post = Post.objects.get(id= post_id)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
    # If the form is valid
        if form.is_valid():
            #yes, save
            form.save()
          # Redirect to home
            return HttpResponseRedirect('/')

        else:
            # no, Show Error
            return HttpResponseRedirect(form.erros.as_json())


    # Show
    return render(request, 'edit.html', {'post': post})


