# -*- coding: utf-8 -*-
from cms.models import get_plugin_media_path, CMSPlugin, Page
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _


@python_2_unicode_compatible
class Teaser(CMSPlugin):
    """
    A Teaser
    """
    title = models.CharField(_("title"), max_length=255)

    image = models.ImageField(
        _("image"), upload_to=get_plugin_media_path, blank=True, null=True)

    page_link = models.ForeignKey(
        Page, verbose_name=_("page"),
        help_text=_("If present image will be clickable"), blank=True,
        null=True, limit_choices_to={'publisher_is_draft': True})

    url = models.CharField(
        _("link"), max_length=255, blank=True, null=True,
        help_text=_("If present image will be clickable."))

    description = models.TextField(_("description"), blank=True, null=True)

    def __str__(self):
        return self.title

    search_fields = ('description',)
