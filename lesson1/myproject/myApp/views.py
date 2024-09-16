from django.shortcuts import render, redirect
from .models import Post
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms


# Create your views here.
def posts_list(req):
    posts = Post.objects.all().order_by("date")
    return render(req, "myApp/posts_list.html", {"posts": posts})


def post_page(req, slug):
    post = Post.objects.get(slug=slug)
    return render(req, "myApp/post_page.html", {"post": post})


@login_required(login_url="/users/login/")
def post_new(req):
    if req.method == "POST":
        form = forms.CreatePost(req.POST, req.FILES)
        if form.is_valid():
            # save with user
            new_post = form.save(commit=False)
            new_post.author = req.user
            new_post.save()
            return redirect("posts:list")
    else:
        form = forms.CreatePost()

    return render(req, "myApp/post_new.html", {"form": form})
