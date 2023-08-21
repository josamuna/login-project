from django.db import models

# Create your models here.
class Login(models.Model):
    fullname = models.CharField(max_length=200, db_column='fullname')
    email = models.EmailField(max_length=200, db_column='email', unique=True)
    password = models.CharField(max_length=200, db_column='password')