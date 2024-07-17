from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.shared.models import AbstractBaseModel


class Education(AbstractBaseModel):
    """
    Education model class.
    """

    school = models.CharField(
        _("School"),
        max_length=255,
        blank=False,
        null=False,
    )
    degree = models.CharField(
        _("Degree"),
        max_length=255,
        blank=False,
        null=False,
    )
    field_of_study = models.CharField(
        _("Field of Study"),
        max_length=255,
        blank=False,
        null=False,
    )
    start_date = models.DateField(
        _("Start Date"),
        blank=False,
        null=False,
    )
    end_date = models.DateField(
        _("End Date"),
        blank=True,
        null=True,
    )
    description = models.TextField(
        _("Description"),
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = _("Education")
        verbose_name_plural = _("Education")

    def __str__(self):
        return f"{self.school}"
