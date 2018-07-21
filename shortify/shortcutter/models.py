from django.db import models


class Shortcut(models.Model):
    long_link = models.CharField(max_length=100, default='', blank=True, null=True)
    short_link = models.CharField(max_length=100, blank=True, null=True, default='')
