from django.db import models

# Create your models here.


class ModelWithFileField(models.Model):
    file_field = models.FileField(upload_to='images/')
