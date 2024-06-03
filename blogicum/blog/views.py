from django.shortcuts import get_object_or_404, render
from django.utils import timezone

from blog.models import Category, Post


def index(request):
    template_name = 'blog/index.html'
    post_list = Post.objects.select_related(
        'category').filter(is_published=True,
                           pub_date__lte=timezone.now(),
                           category__is_published=True)
    context = {'post_list': post_list[:5]}
    return render(request, template_name, context)


def post_detail(request, pk):
    template_name = 'blog/detail.html'
    post = get_object_or_404(
        Post.objects.select_related(
            'category').filter(
                is_published=True,
                pub_date__lte=timezone.now(),
                category__is_published=True), pk=pk)
    context = {'post': post}
    return render(request, template_name, context)


def category_posts(request, category_slug):
    template_name = 'blog/category.html'
    category = get_object_or_404(Category.objects.filter(
        slug=category_slug, is_published=True))
    post_list = category.posts.filter(
        is_published=True, pub_date__lte=timezone.now())
    context = {'category': category, 'post_list': post_list}
    return render(request, template_name, context)
