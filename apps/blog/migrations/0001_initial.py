# Generated by Django 4.0 on 2021-12-20 03:41

import apps.blog.models
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_deleted', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=250)),
                ('image', models.ImageField(default='posts/default.jpg', upload_to=apps.blog.models.upload_to, verbose_name='Image')),
                ('slug', models.SlugField(max_length=250)),
            ],
            options={
                'verbose_name_plural': 'Categories',
                'db_table': 'categories',
            },
        ),
        migrations.CreateModel(
            name='PostModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_deleted', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=250)),
                ('image', models.ImageField(default='posts/default.jpg', upload_to=apps.blog.models.upload_to, verbose_name='Image')),
                ('description', models.TextField(null=True)),
                ('content', models.TextField()),
                ('slug', models.SlugField(max_length=250, unique_for_date='published')),
                ('published', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.CharField(choices=[('published', 'Published'), ('draft', 'Draft')], default='published', max_length=15)),
                ('view_count', models.IntegerField(default=0, editable=False)),
            ],
            options={
                'verbose_name_plural': 'Posts',
                'db_table': 'posts',
                'ordering': ('-published',),
            },
        ),
    ]