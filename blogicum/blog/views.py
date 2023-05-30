from django.shortcuts import get_object_or_404, render
from django.http import HttpRequest, HttpResponse
import datetime as dt

from blog.models import Post, Category

current_datetime = dt.datetime.now()


def index(request: HttpRequest) -> HttpResponse:
    template = 'blog/index.html'
    post_list = (Post.objects.select_related('category')
                 .filter(is_published=True,
                         category__is_published=True,
                         pub_date__lte=current_datetime))[:5]
    context = {'post_list': post_list}
    return render(request, template, context)


def post_detail(request: HttpRequest, id: int) -> HttpResponse:
    template = 'blog/detail.html'
    post = get_object_or_404(Post.objects.filter(
        is_published=True,
        category__is_published=True),
        pub_date__lte=current_datetime,
        pk=id
    )
    context = {'post': post}
    return render(request, template, context)


def category_posts(request: HttpRequest, category_slug: str) -> HttpResponse:
    template = 'blog/category.html'
    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True
    )
    post_list = (Post.objects.select_related('category')
                 .filter(category=category,
                         is_published=True,
                         pub_date__lte=current_datetime))
    context = {'category': category,
               'post_list': post_list}
    return render(request, template, context)
