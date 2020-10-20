from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from django.utils import timezone
from .forms import ProductForm, ProductCommentsForm
# Create your views here.


def product_list(request):
    post = Product.objects.order_by('-publish_date')

    context = {
        'posts': post
    }
    return render(request, 'sales/post_list.html', context)


def product_content(request, pk):
    detail = Product.objects.get(pk=pk)

    context = {
        'detail': detail
    }
    return render(request, 'sales/post_content.html', context)

def add_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid:
            body = form.save(commit=False)
            body.author = request.user
            body.published_date = timezone.now()
            body.save()
            return redirect('product_content', pk=body.pk )

        form = ProductForm()
    else:
        form = ProductForm()
    context = {
        'form': form
    }
    return render(request, 'sales/add_post.html', context)

def product_content_edit(request, pk):
    detail = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=detail)
        if form.is_valid:
            body = form.save(commit=False)
            body.author = request.user
            body.published_date = timezone.now()
            body.save()
            return redirect('product_content', pk=body.pk)

        form = ProductForm()
    else:
        form = ProductForm(instance=detail)
        context = {
            'form': form
        }
        return render(request, 'sales/add_post.html', context)




def add_productcomments(request, pk):
    detail = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        form = ProductCommentsForm(request.POST)
        if form.is_valid:
            comment = form.save(commit=False)
            comment.post = detail
            comment.save()
            return redirect('post_content', pk=detail.pk)
        form = ProductCommentsForm()
    else:
        form = ProductCommentsForm()

    context = {
        'form': form,
        'detail': detail
    }
    return render(request, 'sales/add_comments.html', context)