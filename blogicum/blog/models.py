from django.db import models
from django.contrib.auth import get_user_model

"""Тексты подсказок."""
pub_date_help_text = ('Если установить дату и время в будущем — можно '
                      'делать отложенные публикации.')
slug_help_text = ('Идентификатор страницы для URL; разрешены '
                  'символы латиницы, цифры, дефис и подчёркивание.')
is_published_help_text = ('Снимите галочку, чтобы скрыть публикацию.')

User = get_user_model()


class PublishedModel(models.Model):
    is_published = models.BooleanField(
        default=True,
        verbose_name='Опубликовано',
        help_text=is_published_help_text)
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Добавлено')

    class Meta:
        abstract = True


class Category(PublishedModel):
    title = models.CharField(
        max_length=256,
        verbose_name='Заголовок')
    description = models.TextField(
        verbose_name='Описание')
    slug = models.SlugField(
        unique=True,
        verbose_name='Идентификатор',
        help_text=slug_help_text)

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title


class Location(PublishedModel):
    name = models.CharField(
        max_length=256,
        verbose_name='Название места')

    class Meta:
        verbose_name = 'местоположение'
        verbose_name_plural = 'Местоположения'

    def __str__(self):
        return self.name


class Post(PublishedModel):
    title = models.CharField(
        max_length=256,
        verbose_name='Заголовок')
    text = models.TextField(
        verbose_name='Текст')
    pub_date = models.DateTimeField(
        verbose_name='Дата и время публикации',
        help_text=pub_date_help_text)

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор публикации')
    location = models.ForeignKey(
        Location,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Местоположение')
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        null=True,
        verbose_name='Категория')

    class Meta:
        verbose_name = 'публикация'
        verbose_name_plural = 'Публикации'

    def __str__(self):
        return self.title
