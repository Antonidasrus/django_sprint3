from django.shortcuts import get_object_or_404, render
from django.http import HttpRequest, HttpResponse
from blog.models import Category
from blog.services import get_filtered_queryset

POSTS_VIEWED = 5  # Количество выводимых постов на главной странице


def index(request: HttpRequest) -> HttpResponse:
    template = 'blog/index.html'
    post_list = get_filtered_queryset('category')[:POSTS_VIEWED]
    context = {'post_list': post_list}
    return render(request, template, context)


def post_detail(request: HttpRequest, id: int) -> HttpResponse:
    template = 'blog/detail.html'
    post = get_object_or_404(get_filtered_queryset('category'),
                             pk=id,)
    context = {'post': post}
    return render(request, template, context)


def category_posts(request: HttpRequest, category_slug: str) -> HttpResponse:
    template = 'blog/category.html'
    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True,)
    post_list = get_filtered_queryset('category').filter(category=category,)
    context = {'category': category,
               'post_list': post_list}
    return render(request, template, context)
