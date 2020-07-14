from django.db import models

class Image(models.Model):
    tipo = models.CharField(max_length=70, blank=False, default='')
    color = models.CharField(max_length=70, blank=False, default='')
    created_at = models.DateTimeField(auto_now_add=True)

class Tutorial(models.Model):
    title = models.CharField(max_length=70, blank=False, default='')
    description = models.CharField(max_length=200,blank=False, default='')
    published = models.BooleanField(default=False)