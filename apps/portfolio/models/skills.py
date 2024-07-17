from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.shared.models import AbstractBaseModel


class Skill(AbstractBaseModel):
    name = models.CharField(max_length=255, verbose_name=_("name"))
    percentage = models.PositiveIntegerField(verbose_name=_("percentage"))
    image = models.ImageField(upload_to="skills/", verbose_name=_("image"))

    class Meta:
        verbose_name = _("skill")
        verbose_name_plural = _("skills")

    def __str__(self):
        return self.name
