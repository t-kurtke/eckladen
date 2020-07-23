from django.shortcuts import render
from blog.models import Post, Category, Comment
from blog.forms import CommentForm
# Create your views here.
def blog_index(request):
    posts = Post.objects.all().order_by('-created_on')
    context = {
        'posts': posts,
    }
    return render(request, 'blog_index.html', context)

def blog_detail(request, pk):
    post = Post.objects.get(pk=pk)

    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(author=form.cleaned_data['author'],
            body=form.cleaned_data['body'],
            post=post)
            comment.save()

    comments = Comment.objects.filter(post=post)
    context = {
        'comments': comments,
        'post': post,
        'form': form,
    }
    return render(request, 'blog_detail.html', context)

def blog_category(request, category_name): # argument name defined in urls.py can only be part of url
    posts = Post.objects.filter(categories__name__contains=category_name).order_by('-created_on')
    context = {
        'category_name': category_name,
        'posts': posts,
    }
    return render(request, 'blog_category.html', context)