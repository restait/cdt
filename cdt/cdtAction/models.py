from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.contenttypes.fields import GenericRel
from django.contrib.contenttypes.models import ContentType


@python_2_unicode_compatible
class User(models.Model):
    name = models.CharField(max_length=64, null=True)
    email = models.CharField(max_length=64, null=True, unique=True)

    def __str__(self):
        return self.email
