from django.shortcuts import render, redirect
from blog.models import Post, Category, Comment, PostImage
from blog.forms import CommentForm, FileFieldForm, CategoryForm
from django.contrib.auth.mixins import LoginRequiredMixin
from guardian.shortcuts import assign_perm
from guardian.mixins import PermissionRequiredMixin
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse
from django.http import HttpResponseRedirect
# Create your views here.

class PostCreate(LoginRequiredMixin, CreateView):
    model = Post
    template_name_suffix = "_create_form"
    fields = ["title", "body"]

    def form_valid(self, form):
        form.instance.user = self.request.user
        post = form.save()
        category_form = CategoryForm(self.request.POST)
        if category_form.is_valid():
            post.categories.set([category_form.save(),])
        post.save()
        if self.request.FILES:
            for f in self.request.FILES.getlist('file_field'):
                image = PostImage()
                image.image = f
                image.post = post
                image.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(PostCreate, self).get_context_data(**kwargs)
        context['file_form'] = FileFieldForm
        context['category_form'] = CategoryForm
        return context
    def get_success_url(self):
        return reverse(blog_detail, kwargs={'pk':self.object.pk})

class PostUpdate(PermissionRequiredMixin, UpdateView):
    model = Post
    template_name_suffix = "_update_form"
    fields = ["title", "body"]
    permission_required = "change_post"
    def form_valid(self, form):
        form.instance.user = self.request.user
        post = form.save()
        category_form = CategoryForm(self.request.POST)
        if category_form.is_valid():
            post.categories.set([category_form.save(),])
        post.save()
        if self.request.FILES:
            for f in self.request.FILES.getlist('file_field'):
                image = PostImage()
                image.image = f
                image.post = post
                image.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(PostUpdate, self).get_context_data(**kwargs)
        images =  PostImage.objects.filter(post=self.object)
        context['images'] = images
        context['file_form'] = FileFieldForm
        context['category_form'] = CategoryForm
        return context
    def get_success_url(self):
        return reverse(blog_detail, kwargs={'pk':self.object.pk})

def postimage_delete(request, pk):
    postimage = PostImage.objects.get(pk=pk)
    post = postimage.post
    postimage.delete()
    return HttpResponseRedirect(reverse('post_update', kwargs={'pk':post.pk}))

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
    images = PostImage.objects.filter(post=post)
    context = {
        'comments': comments,
        'post': post,
        'images': images,
        'form': form,
    }
    return render(request, 'blog_detail.html', context)

def blog_category(request, category_name): # argument name defined in urls.py can only be part of url
    posts = Post.objects.filter(categories__category__contains=category_name).order_by('-created_on')
    context = {
        'category_name': category_name,
        'posts': posts,
    }
    return render(request, 'blog_category.html', context)

def posts_user(request, user_name):
    posts = Post.objects.filter(user__username__contains=user_name)

    context = {
        "posts": posts

        }
    return render(request, "blog_index.html", context)

@receiver(post_save, sender=Post)
def set_permission(sender, instance, **kwargs):
    """Add object specific permission to the author"""
    assign_perm(
        "change_post",  # The permission we want to assign.
        instance.user,  # The user object.
        instance  # The object we want to assign the permission to.
    )
    assign_perm(
        "delete_post",  # The permission we want to assign.
        instance.user,  # The user object.
        instance  # The object we want to assign the permission to.
    )