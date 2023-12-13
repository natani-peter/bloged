from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from . import models
from . import forms


# Create your views here.

def index(request):
    return render(request, 'blogs/index.html')


def home(request):
    posts = models.BlogPost.objects.all().order_by('-date_added')
    context = {'posts': posts}
    return render(request, 'blogs/home.html', context)


def full_article(request, post_id):
    wanted_post = get_object_or_404(models.BlogPost, id=post_id)
    post_article = wanted_post.text
    context = {'post': wanted_post, "article": post_article}
    return render(request, 'blogs/article.html', context)


@login_required(login_url="users:login")
def add_topic(request):
    if request.method != 'POST':
        form = forms.BlogPostForm()
    else:
        form = forms.BlogPostForm(data=request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.owner = request.user
            new_post.save()
            return redirect('blogs:home')
    context = {'form': form}
    return render(request, 'blogs/add_post.html', context)


@login_required(login_url="users:login")
def edit_post(request, post_id):
    post_to_be_edited = get_object_or_404(models.BlogPost, id=post_id)
    if request.user != post_to_be_edited.owner:
        raise Http404()
    if request.method != 'POST':
        form = forms.BlogPostForm(instance=post_to_be_edited)
    else:
        form = forms.BlogPostForm(instance=post_to_be_edited, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("blogs:article", post_id)
    context = {'form': form, 'post': post_to_be_edited}
    return render(request, 'blogs/edit_post.html', context)


@login_required()
def delete_post(request, post_id):
    to_be_deleted = get_object_or_404(models.BlogPost, id=post_id)

    if request.user != to_be_deleted.owner:
        raise Http404()

    if request.method == 'POST':
        to_be_deleted.delete()
        return redirect("blogs:home")
    context = {'post': to_be_deleted}
    return render(request, "blogs/delete_post.html", context)
