# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2017-02-25 11:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("cms_articles", "0007_plugins"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="article",
            options={
                "ordering": ("-order_date",),
                "permissions": (("publish_article", "Can publish article"),),
                "verbose_name": "article",
                "verbose_name_plural": "articles",
            },
        ),
        migrations.AddField(
            model_name="article",
            name="revision_id",
            field=models.PositiveIntegerField(default=0, editable=False),
        ),
        migrations.AlterField(
            model_name="articleplugin",
            name="cmsplugin_ptr",
            field=models.OneToOneField(
                auto_created=True,
                on_delete=django.db.models.deletion.CASCADE,
                parent_link=True,
                primary_key=True,
                related_name="cms_articles_articleplugin",
                serialize=False,
                to="cms.CMSPlugin",
            ),
        ),
        migrations.AlterField(
            model_name="articlescategoryplugin",
            name="cmsplugin_ptr",
            field=models.OneToOneField(
                auto_created=True,
                on_delete=django.db.models.deletion.CASCADE,
                parent_link=True,
                primary_key=True,
                related_name="cms_articles_articlescategoryplugin",
                serialize=False,
                to="cms.CMSPlugin",
            ),
        ),
        migrations.AlterField(
            model_name="articlesplugin",
            name="cmsplugin_ptr",
            field=models.OneToOneField(
                auto_created=True,
                on_delete=django.db.models.deletion.CASCADE,
                parent_link=True,
                primary_key=True,
                related_name="cms_articles_articlesplugin",
                serialize=False,
                to="cms.CMSPlugin",
            ),
        ),
        migrations.AlterField(
            model_name="articlesplugin",
            name="trees",
            field=models.ManyToManyField(
                blank=True,
                limit_choices_to={
                    "application_urls": "CMSArticlesApp",
                    "node__site_id": 1,
                    "publisher_is_draft": False,
                },
                related_name="_articlesplugin_trees_+",
                to="cms.Page",
                verbose_name="trees",
            ),
        ),
    ]
