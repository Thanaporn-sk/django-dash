__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = 'Copyright (c) 2013 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('Bookmark',)

from django.db import models
from django.utils.translation import ugettext_lazy as _

from dash.contrib.plugins.url.settings import BOOKMARK_IMAGE_CHOICES_WITH_EMPTY_OPTION

class Bookmark(models.Model):
    """
    Bookmark.

    - `title` (string): Bookmark title.
    - `url` (string): Bookmark URL.
    - `external` (bool): External/internal link.
    - `image` (string): Bookmark image icon.
    """
    title = models.CharField(_("Title"), max_length=100)
    url = models.URLField(_("URL"), max_length=255)
    external = models.BooleanField(_("External"), default=False)
    image = models.CharField(_("Image"), max_length=255, blank=True, null=True, \
                             choices=BOOKMARK_IMAGE_CHOICES_WITH_EMPTY_OPTION)

    class Meta:
        verbose_name = _("Bookmark")
        verbose_name_plural = _("Bookmarks")

    def __unicode__(self):
        return self.title
