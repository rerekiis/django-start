from django.db import models

# Create your models here.

class Person(models.Model):
    nick_name = models.CharField(max_length=16)
    first_name = models.CharField(max_length=16)
    last_name = models.CharField(max_length=16)
    avatar = models.ImageField(upload_to="avatars/%Y/%m/%d", blank=True, null=True)
    about = models.TextField(blank=True, null=True)


    
