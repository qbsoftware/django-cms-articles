from django.contrib.sites.models import Site
from django.db import models
from django.utils.encoding import force_text, python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

from ..conf import settings


@python_2_unicode_compatible
class Attribute(models.Model):
    site = models.ForeignKey(Site, on_delete=models.CASCADE, default=settings.SITE_ID)
    name = models.CharField(_("name"), max_length=255)

    class Meta:
        app_label = "cms_articles"
        unique_together = (("site", "name"),)
        verbose_name = _("attribute")
        verbose_name_plural = _("attributes")

    def __str__(self):
        return force_text(self.name)
