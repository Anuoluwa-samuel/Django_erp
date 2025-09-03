from django.db import models

class SiteSetting(models.Model):
    name = models.CharField(max_length=100)
    color = ColorField(default="")