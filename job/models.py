from django.db import models
'''
    - html widet
    - validation
    - db size
'''
# Create your models here.
class Job(models.Model):
    title = models.CharField(max_length=100)
