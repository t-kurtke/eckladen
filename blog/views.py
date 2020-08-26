from django.shortcuts import render
from blog.models import Post, Category, Comment, PostImage
from blog.forms import CommentForm, FileFieldForm, CategoryForm
from django.contrib.auth.mixins import LoginRequiredMixin
from guardian.shortcuts import assign_perm
from guardian.mixins import PermissionRequiredMixin
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse

# Create your views here.

class PostCreate(LoginRequiredMixin, CreateView):
    model = Post
    template_name_suffix = "_create_form"
    fields = ["title", "body"]

    def form_valid(self, form):
        form.instance.user = self.request.user
        post = form.save(commit=False)
        if self.request.FILES:
            for f in self.request.FILES.getlist('file'):
                image = PostImage()
                image.image = f
                image.post = post
        return super().form_valid(form)
    def get_context_data(self, **kwargs):
        context = super(PostCreate, self).get_context_data(**kwargs)
        context['file_form'] = FileFieldForm
        context['category_form'] = CategoryForm
        return context
    def get_success_url(self):
        return reverse(blog_detail, kwargs={'pk':self.object.pk})

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