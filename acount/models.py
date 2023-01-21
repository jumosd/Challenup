from django.db import models

# Create your models here.

class User(models.Model):
    user_id = models.CharField(max_length=20)
    user_name = models.CharField(max_length=20)
    user_password = models.CharField(max_length=20)



