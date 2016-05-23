# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-20 20:00
from __future__ import unicode_literals

import cms.models.fields
from cms.models import Page
from cms_articles.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import filer.fields.folder


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('filer', '0002_auto_20150606_2003'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cms_articles', '0004_categories'),
        ('cms', '0013_urlconfrevision'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_id', models.IntegerField(unique=True, verbose_name='author id')),
                ('login', models.CharField(max_length=255, verbose_name='login name')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='email')),
                ('first_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='last name')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name': 'author',
                'verbose_name_plural': 'authors',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('term_id', models.IntegerField(unique=True, verbose_name='term id')),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('slug', models.SlugField(verbose_name='slug')),
                ('parent', models.CharField(blank=True, max_length=255, null=True, verbose_name='parent slug')),
                ('cached_name', models.CharField(blank=True, max_length=512, null=True, verbose_name='name')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='cms_articles.Category', verbose_name='articles category')),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(default='', verbose_name='title')),
                ('link', models.CharField(max_length=255, verbose_name='link')),
                ('pub_date', models.DateTimeField(verbose_name='publication date')),
                ('guid', models.CharField(max_length=255, verbose_name='url')),
                ('description', models.TextField(verbose_name='description')),
                ('content', models.TextField(verbose_name='content')),
                ('excerpt', models.TextField(verbose_name='excerpt')),
                ('post_id', models.IntegerField(unique=True, verbose_name='post id')),
                ('post_date', models.DateTimeField(verbose_name='post date')),
                ('post_name', models.CharField(max_length=255, verbose_name='post name')),
                ('status', models.CharField(max_length=20, verbose_name='status')),
                ('post_parent', models.IntegerField(verbose_name='parent post id')),
                ('post_type', models.CharField(max_length=20, verbose_name='type')),
                ('postmeta', models.TextField(verbose_name='metadata')),
                ('article', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='cms_articles.Article', verbose_name='imported article')),
                ('categories', models.ManyToManyField(blank=True, related_name='kategorie', to='import_wordpress.Category')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='import_wordpress.Author', verbose_name='created by')),
                ('file', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='filer.File', verbose_name='imported file')),
                ('folder', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='filer.Folder', verbose_name='attachments folder')),
                ('page', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='cms.Page', verbose_name='imported page')),
            ],
            options={
                'verbose_name': 'item',
                'verbose_name_plural': 'items',
            },
        ),
        migrations.CreateModel(
            name='Options',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='name')),
                ('language', models.CharField(help_text='The language of the content fields.', max_length=15, verbose_name='language')),
                ('article_template', models.CharField(choices=settings.CMS_ARTICLES_TEMPLATES, default=settings.CMS_ARTICLES_TEMPLATES[0][0], max_length=100, verbose_name='template')),
                ('article_slot', models.CharField(default='content', help_text='The name of placeholder used to create content plugins in.', max_length=255, verbose_name='slot')),
                ('article_redirects', models.BooleanField(default=True, help_text='Create django redirects for each article from the old path to the new imported path', verbose_name='create redirects')),
                ('article_publish', models.BooleanField(default=False, help_text='Publish imported articles.', verbose_name='publish')),
                ('page_template', models.CharField(choices=Page.template_choices, default=Page.TEMPLATE_DEFAULT, max_length=100, verbose_name='template')),
                ('page_slot', models.CharField(default='content', help_text='The name of placeholder used to create content plugins in.', max_length=255, verbose_name='slot')),
                ('page_redirects', models.BooleanField(default=True, help_text='Create django redirects for each page from the old path to the new imported path', verbose_name='create redirects')),
                ('page_publish', models.BooleanField(default=False, help_text='Publish imported pages.', verbose_name='publish')),
                ('article_folder', filer.fields.folder.FilerFolderField(blank=True, help_text='Select folder for articles. Subfolder will be created for each article with attachments.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='filer.Folder', verbose_name='attachments folder')),
                ('article_tree', models.ForeignKey(help_text='All posts will be imported as articles in this tree.', on_delete=django.db.models.deletion.CASCADE, related_name='+', to='cms.Page', verbose_name='tree')),
                ('file_folder', filer.fields.folder.FilerFolderField(blank=True, help_text='Select folder for other attachments.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='filer.Folder', verbose_name='folder')),
                ('gallery_folder', filer.fields.folder.FilerFolderField(blank=True, help_text='Select folder for galleries. Subfolder will be created for each gallery.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='filer.Folder', verbose_name='folder')),
                ('page_folder', filer.fields.folder.FilerFolderField(blank=True, help_text='Select folder for pages. Subfolder will be created for each page with attachments.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='filer.Folder', verbose_name='attachments folder')),
                ('page_root', cms.models.fields.PageField(blank=True, help_text='All pages will be imported as sub-pages of this page.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='cms.Page', verbose_name='root')),
                ('slide_folder', filer.fields.folder.FilerFolderField(blank=True, help_text='Select folder for slides.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='filer.Folder', verbose_name='folder')),
            ],
            options={
                'verbose_name': 'options',
                'verbose_name_plural': 'options',
            },
        ),
    ]