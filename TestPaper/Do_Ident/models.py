from django.db import models
import django.utils.timezone as timezone
from django.contrib import admin

# Create your models here.
class TestPaper(models.Model):
    title = models.CharField(max_length = 150, default=None)
    paper_idx = models.CharField(max_length=64, default=None, unique=True)
    result = models.CharField(max_length=64, default=None)
    timestamp = models.DateTimeField(default=timezone.now)
    class Meta:
        ordering = ['-timestamp']