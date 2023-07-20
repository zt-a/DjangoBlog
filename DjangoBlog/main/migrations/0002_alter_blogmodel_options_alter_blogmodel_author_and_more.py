# Generated by Django 4.2.3 on 2023-07-17 11:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogmodel',
            options={'verbose_name': 'Блог', 'verbose_name_plural': 'Блоги'},
        ),
        migrations.AlterField(
            model_name='blogmodel',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор'),
        ),
        migrations.AlterField(
            model_name='blogmodel',
            name='content',
            field=models.TextField(verbose_name='Контент'),
        ),
        migrations.AlterField(
            model_name='blogmodel',
            name='slug',
            field=models.SlugField(max_length=100, unique=True, verbose_name='URL'),
        ),
        migrations.AlterField(
            model_name='blogmodel',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Заголовок'),
        ),
    ]