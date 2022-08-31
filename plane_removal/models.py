from django.db import models

# Create your models here.
class PCFile(models.Model):
    name = models.CharField(max_length=200)
    file = models.FileField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self) -> str:
        return self.name


class ConfigFile(models.Model):
    name = models.CharField(max_length=200)
    file = models.FileField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self) -> str:
        return self.name