import datetime as dt
from blog.models import Post


def get_filtered_queryset(param: str):
    return (Post.objects.select_related(param)
            .filter(is_published=True,
                    category__is_published=True,
                    pub_date__lte=dt.datetime.now(),)
            .only('category', 'title', 'text', 'pub_date'))
