from django.db import models
from django.contrib.auth import get_user_model
from blog.hints import HelpText

User = get_user_model()
hints = HelpText()


class PublishedModel(models.Model):
    is_published = models.BooleanField(
        default=True,
        verbose_name='Опубликовано',
        help_text=hints.print_hint('is_published'),)
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Добавлено',)

    class Meta:
        abstract = True


class Category(PublishedModel):
    title = models.CharField(
        max_length=256,
        verbose_name='Заголовок',)
    description = models.TextField(
        verbose_name='Описание',)
    slug = models.SlugField(
        unique=True,
        verbose_name='Идентификатор',
        help_text=hints.print_hint('slug'),)

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'Категории'

    def __str__(self) -> str:
        return self.title


class Location(PublishedModel):
    name = models.CharField(
        max_length=256,
        verbose_name='Название места',)

    class Meta:
        verbose_name = 'местоположение'
        verbose_name_plural = 'Местоположения'

    def __str__(self) -> str:
        return self.name


class Post(PublishedModel):
    title = models.CharField(
        max_length=256,
        verbose_name='Заголовок',)
    text = models.TextField(
        verbose_name='Текст')
    pub_date = models.DateTimeField(
        verbose_name='Дата и время публикации',
        help_text=hints.print_hint('pub_date'),)

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор публикации',)
    location = models.ForeignKey(
        Location,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Местоположение',)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        null=True,
        verbose_name='Категория',)

    class Meta:
        verbose_name = 'публикация'
        verbose_name_plural = 'Публикации'
        ordering = ['-pub_date']

    def __str__(self) -> str:
        return self.title
