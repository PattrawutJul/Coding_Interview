from django.db import models

class match(models.Model):
    message = models.CharField(max_length=2000)
    pattern = models.CharField(max_length=2000)
    

