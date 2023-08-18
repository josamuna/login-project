from django.db import models

# Create your models here.
class Login(models.Model):
    fullname = models.CharField(max_length=200, db_column='fullname')
    username = models.CharField(max_length=200, db_column='username')
    email = models.CharField(max_length=200, db_column='email')
    password = models.CharField(max_length=200, db_column='password')