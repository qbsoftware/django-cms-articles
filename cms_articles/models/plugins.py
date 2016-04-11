from __future__ import absolute_import, division, generators, nested_scopes, print_function, unicode_literals, with_statement

from cms.models import CMSPlugin
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.functional import cached_property
from django.utils.translation import get_language, ugettext_lazy as _

from ..conf import settings

from .article import Article



@python_2_unicode_compatible
class ArticlePlugin(CMSPlugin):
    article     = models.ForeignKey(Article)
    template    = models.CharField(_('Template'), max_length = 100,
        choices     = settings.CMS_ARTICLES_PLUGIN_ARTICLE_TEMPLATES,
        default     = settings.CMS_ARTICLES_PLUGIN_ARTICLE_TEMPLATES[0][0],
        help_text   = _('The template used to render plugin.'),
    )

    def __str__(self):
        return self.article.get_title()

    @cached_property
    def render_template(self):
        return 'cms_articles/article/%s.html' % self.template



@python_2_unicode_compatible
class ArticlesPlugin(CMSPlugin):
    number      = models.IntegerField(_('Number of last articles'), default = 3)
    template    = models.CharField(_('Template'), max_length = 100,
        choices     = settings.CMS_ARTICLES_PLUGIN_ARTICLES_TEMPLATES,
        default     = settings.CMS_ARTICLES_PLUGIN_ARTICLES_TEMPLATES[0][0],
        help_text=_('The template used to render plugin.'),
    )

    def __str__(self):
        return _('last {} articles').format(self.number)

    @cached_property
    def articles(self):
        page = self.placeholder.page
        if page.publisher_is_draft:
            return Article.objects.drafts().filter(category=page.get_public_object()).order_by('-publication_date')[:self.number]
        else:
            return Article.objects.public().filter(category=page).order_by('-publication_date')[:self.number]

    @cached_property
    def render_template(self):
        return 'cms_articles/articles/%s.html' % self.template


