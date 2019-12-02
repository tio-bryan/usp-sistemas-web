from django.db import models


class File(models.Model):
    name = models.CharField(max_length=500)
    filepath = models.FileField(null=True, verbose_name="")
    owner = models.CharField(max_length=500)