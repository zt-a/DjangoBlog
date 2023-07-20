# Generated by Django 4.2.3 on 2023-07-17 10:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('slug', models.SlugField(unique=True, verbose_name='URL')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Время создание')),
                ('time_update', models.DateTimeField(auto_now=True, verbose_name='Время обновление')),
                ('is_published', models.BooleanField(default=True, verbose_name='Публикация')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='ContactUsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Ваше имя')),
                ('email', models.EmailField(max_length=255, verbose_name='Ваш Email')),
                ('message', models.TextField(verbose_name='Сообщение')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Время создание')),
                ('time_update', models.DateTimeField(auto_now=True, verbose_name='Время обновление')),
                ('is_published', models.BooleanField(default=True, verbose_name='Публикация')),
            ],
            options={
                'verbose_name': 'Обратная связь',
                'verbose_name_plural': 'Обратные связи',
                'ordering': ['-time_create', 'id'],
            },
        ),
        migrations.CreateModel(
            name='TagModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Имя тега')),
                ('slug', models.SlugField(unique=True, verbose_name='URL')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Время создание')),
                ('time_update', models.DateTimeField(auto_now=True, verbose_name='Время обновление')),
                ('is_published', models.BooleanField(default=True, verbose_name='Публикация')),
            ],
            options={
                'verbose_name': 'Тег',
                'verbose_name_plural': 'Теги',
                'ordering': ['-time_create', 'id'],
            },
        ),
        migrations.CreateModel(
            name='BlogModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('content', models.TextField()),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Время создание')),
                ('time_update', models.DateTimeField(auto_now=True, verbose_name='Время обновление')),
                ('is_published', models.BooleanField(default=True, verbose_name='Публикация')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Blogs',
            },
        ),
    ]
