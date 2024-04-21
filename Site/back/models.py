from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Users(AbstractUser):
        id = models.AutoField(primary_key=True)
        username = models.CharField(max_length=100, null=True)
        email = models.CharField(max_length=100, null=True)
        password = models.CharField(max_length=500, null=True)
        created_at = models.DateTimeField(auto_now_add=True , null=True)

        class Meta:
                managed = False
                db_table = 'users'
                ordering = ['created_at']
        
        def __str__(self):
                return self.username

class Logg(models.Model):
        id = models.AutoField(primary_key=True)
        log = models.CharField(max_length=500, null=True)
        created_at = models.DateTimeField(auto_now_add=True , null=True)

        class Meta:
                managed = False
                db_table = 'logg'
                ordering = ['created_at']

        def __str__(self):
                return self.id

