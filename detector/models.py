from django.db import models

# import os
# def upload_path(instance, filename):
#     return filename

# Create your models here.
class ImageModel(models.Model):
    image = models.ImageField(null=False, blank=True)
    created_date = models.DateTimeField(null=False, blank=True, auto_now_add=True)

    def __str__(self):
        return self.image.url