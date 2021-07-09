from django.db import models

# Create your models here.


class Movie(models.Model):
    name = models.CharField(max_length=200, null=False)
    description = models.TextField(null=False)
    trailer = models.CharField(max_length=200, null=False)
    year = models.IntegerField(null=False)
    start = models.IntegerField(null=False)
    show = models.BooleanField(default=True)

    def __str__(self):
        return self.name
