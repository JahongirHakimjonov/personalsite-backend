from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.shared.models import AbstractBaseModel


class ContactInfo(AbstractBaseModel):
    email = models.EmailField(unique=True, verbose_name=_("Email"))
    phone = models.CharField(max_length=20, verbose_name=_("Phone"))
    address = models.CharField(max_length=255, verbose_name=_("Address"))
    city = models.CharField(max_length=50, verbose_name=_("City"))
    instagram = models.URLField(blank=True, null=True, verbose_name=_("Instagram"))
    facebook = models.URLField(blank=True, null=True, verbose_name=_("Facebook"))
    twitter = models.URLField(blank=True, null=True, verbose_name=_("Twitter"))
    linkedin = models.URLField(blank=True, null=True, verbose_name=_("Linkedin"))
    telegram = models.URLField(blank=True, null=True, verbose_name=_("Telegram"))
    site = models.URLField(blank=True, null=True, verbose_name=_("Site"))
    github = models.URLField(blank=True, null=True, verbose_name=_("Github"))
    gitlab = models.URLField(blank=True, null=True, verbose_name=_("Gitlab"))
    resume = models.FileField(
        upload_to="resume/", blank=True, null=True, verbose_name=_("Resume")
    )
    resume_url = models.URLField(blank=True, null=True, verbose_name=_("Resume URL"))
