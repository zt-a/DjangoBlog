from django.db import models
from django.urls import reverse
from django.utils.text import slugify

class Category(models.Model):
    name = models.CharField(verbose_name='Название', max_length=100)
    slug = models.SlugField(verbose_name='URL', unique=True)

    time_create = models.DateTimeField(verbose_name='Время создание', auto_now_add=True)
    time_update = models.DateTimeField(verbose_name='Время обновление', auto_now=True)
    is_published = models.BooleanField(verbose_name='Публикация', default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def get_absolute_url(self):
        return reverse('categories', kwargs={'slug': self.slug})


class ContactUsModel(models.Model):
    name = models.CharField(verbose_name='Ваше имя', max_length=255)
    email = models.EmailField(verbose_name='Ваш Email', max_length=255)
    message = models.TextField(verbose_name='Сообщение')


    time_create = models.DateTimeField(verbose_name='Время создание', auto_now_add=True)
    time_update = models.DateTimeField(verbose_name='Время обновление', auto_now=True)
    is_published = models.BooleanField(verbose_name='Публикация', default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Обратная связь'
        verbose_name_plural = 'Обратные связи'
        ordering = ['-time_create', 'id']

class TagModel(models.Model):
    name = models.CharField(verbose_name='Имя тега', max_length=50, unique=True)
    slug = models.SlugField(verbose_name='URL', max_length=50, unique=True)

    time_create = models.DateTimeField(verbose_name='Время создание', auto_now_add=True)
    time_update = models.DateTimeField(verbose_name='Время обновление', auto_now=True)
    is_published = models.BooleanField(verbose_name='Публикация', default=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('tags', kwargs={'slug': self.slug})

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'
        ordering = ['-time_create', 'id']


class BlogModel(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    slug = models.SlugField(max_length=255, unique=True, verbose_name='URL')
    content = models.TextField(verbose_name='Контент')
    categories = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, verbose_name='Категории')
    tags = models.ManyToManyField(TagModel, verbose_name='Теги')
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name='Автор')
    time_create = models.DateTimeField(verbose_name='Время создание', auto_now_add=True)
    time_update = models.DateTimeField(verbose_name='Время обновление', auto_now=True)
    is_published = models.BooleanField(verbose_name='Публикация', default=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('blogs/', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блоги'