# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-16 14:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion

from cms_articles.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ("cms", "0001_initial"),
        ("cms_articles", "0003_description_image"),
    ]

    operations = [
        migrations.RenameField(
            model_name="article",
            old_name="category",
            new_name="tree",
        ),
        migrations.RenameField(
            model_name="articlesplugin",
            old_name="category",
            new_name="tree",
        ),
        migrations.AlterField(
            model_name="article",
            name="tree",
            field=models.ForeignKey(
                help_text="The page the article is accessible at.",
                limit_choices_to={
                    "application_urls": "CMSArticlesApp",
                    "node__site_id": 1,
                    "publisher_is_draft": False,
                },
                on_delete=django.db.models.deletion.CASCADE,
                related_name="cms_articles",
                to="cms.Page",
                verbose_name="tree",
            ),
        ),
        migrations.AlterField(
            model_name="articlesplugin",
            name="tree",
            field=models.ForeignKey(
                blank=True,
                help_text="Keep empty to show articles from current page, if current page is a tree.",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="+",
                to="cms.Page",
                verbose_name="tree",
            ),
        ),
        migrations.CreateModel(
            name="Category",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                (
                    "page",
                    models.OneToOneField(
                        limit_choices_to={"node__site_id": 1, "publisher_is_draft": True},
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="cms_articles_category",
                        to="cms.Page",
                        verbose_name="page",
                    ),
                ),
            ],
            options={
                "verbose_name": "category",
                "verbose_name_plural": "categories",
            },
        ),
        migrations.AddField(
            model_name="article",
            name="categories",
            field=models.ManyToManyField(
                blank=True, related_name="articles", to="cms_articles.Category", verbose_name="categories"
            ),
        ),
        migrations.AddField(
            model_name="articlesplugin",
            name="categories",
            field=models.ManyToManyField(
                blank=True,
                related_name="_articlesplugin_categories_+",
                to="cms_articles.Category",
                verbose_name="categories",
            ),
        ),
        migrations.CreateModel(
            name="ArticlesCategoryPlugin",
            fields=[
                (
                    "cmsplugin_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="cms.CMSPlugin",
                    ),
                ),
                ("number", models.IntegerField(default=3, verbose_name="Number of last articles")),
                (
                    "template",
                    models.CharField(
                        choices=settings.CMS_ARTICLES_PLUGIN_ARTICLES_TEMPLATES,
                        default=settings.CMS_ARTICLES_PLUGIN_ARTICLES_TEMPLATES[0][0],
                        help_text="The template used to render plugin.",
                        max_length=100,
                        verbose_name="Template",
                    ),
                ),
                (
                    "subcategories",
                    models.BooleanField(
                        default=False,
                        help_text="Check, if you want to include articles from sub-categories of this category.",
                        verbose_name="include sub-categories",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=("cms.cmsplugin",),
        ),
    ]
