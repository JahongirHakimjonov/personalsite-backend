from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.shared.models import AbstractBaseModel


class Home(AbstractBaseModel):
    title = models.CharField(max_length=255, verbose_name=_("title"))
    subtitle = models.CharField(max_length=255, verbose_name=_("subtitle"))
    description = models.TextField(verbose_name=_("description"))
    image = models.ImageField(upload_to="home/", verbose_name=_("image"))

    class Meta:
        verbose_name = _("home")
        verbose_name_plural = _("home")

    def __str__(self):
        return self.title
