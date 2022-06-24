from dataclasses import Field
from lib2to3.pytree import Base
from django.db import models

# Create your models here.
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.contrib.settings.models import BaseSetting, register_setting

@register_setting
class SocialMediaSettings(BaseSetting):
    instagram = models.URLField(max_length=100)
    panels = [
        FieldPanel("instagram")
    ]