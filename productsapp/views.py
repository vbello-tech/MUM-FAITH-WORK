from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comments
from django.utils import timezone
from .forms import PostForm, CommentsForm
# Create your views here.

def homepage(request):
    return render(request, 'home.html')

def add_all_post(request):
    return render(request, 'add_all_post.html')

def about(request):
    return render(request, 'about.html')

def post_list(request):
    post = Post.objects.order_by('-publish_date')

    context = {
        'posts':post
    }
    return render(request, 'products/post_list.html', context)


def post_content(request, pk):
    detail = Post.objects.get(pk=pk)

    context = {
        'detail': detail
    }
    return render(request, 'products/post_content.html', context)

def add_post(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid:
            body = form.save(commit=False)
            body.author = request.user
            body.published_date = timezone.now()
            body.save()
            return redirect('post_content', pk=body.pk)
        form = PostForm()
    else:
        form = PostForm()

    context = {
        'form': form
    }
    return render(request, 'products/add_post.html', context)

def post_content_edit(request, pk):
    detail = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=detail)
        if form.is_valid:
            body = form.save(commit=False)
            body.author = request.user
            body.published_date = timezone.now()
            body.save()
            return redirect('post_content', pk=body.pk)
        form = PostForm()
    else:
        form = PostForm(instance=detail)

    context = {
        'form': form
    }
    return render(request, 'products/add_post.html', context)


def add_comments(request, pk):
    detail = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentsForm(request.POST)
        if form.is_valid:
            comment = form.save(commit=False)
            comment.post = detail
            comment.save()
            return redirect('post_content', pk=detail.pk)
        form = CommentsForm()
    else:
        form = CommentsForm()

    context = {
        'form': form,
        'detail': detail
    }
    return render(request, 'products/add_comments.html', context)



