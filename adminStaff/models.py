from django.db import models

# Create your models here.
class TemplateNoticeMessage(models.Model):
    title = models.CharField(blank=False,max_length=30)
    message = models.TextField(blank=False)

