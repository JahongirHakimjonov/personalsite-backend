from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.shared.models import AbstractBaseModel


class Project(AbstractBaseModel):
    title = models.CharField(max_length=255, verbose_name=_("Title"))
    name = models.CharField(max_length=255, verbose_name=_("Name"))
    my_role = models.CharField(max_length=255, verbose_name=_("My Role"))
    url = models.URLField(verbose_name=_("URL"), blank=True, null=True)
    description = models.TextField(verbose_name=_("Description"))
    description = models.ImageField(upload_to="projects/", verbose_name=_("Image"))
    tools = models.ManyToManyField("Skill", verbose_name=_("Tools"))
    date = models.DateField(verbose_name=_("Date"))
