from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.shared.models import AbstractBaseModel


class Experience(AbstractBaseModel):
    title = models.CharField(_("Title"), max_length=255)
    company = models.CharField(_("Company"), max_length=255)
    degree = models.CharField(_("Degree"), max_length=255)
    location = models.CharField(_("Location"), max_length=255)
    start_date = models.CharField(_("Start Date"), max_length=255)
    end_date = models.CharField(_("End Date"), max_length=255)
    description = models.TextField(_("Description"))

    class Meta:
        verbose_name = _("Experience")
        verbose_name_plural = _("Experiences")

    def __str__(self):
        return self.title
