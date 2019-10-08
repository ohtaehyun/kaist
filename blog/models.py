from django.db import models

# Create your models here.


class post(models.Model):
    title = models.CharField(verbose_name="제목", max_length=50)
    pass
