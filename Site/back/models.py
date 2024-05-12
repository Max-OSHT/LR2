from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager as AbstractUserManager

class Users(AbstractUser):
        id = models.AutoField(primary_key=True)
        username = models.CharField(max_length=100, null=True, unique=True)
        email = models.CharField(max_length=100, null=True)
        password = models.CharField(max_length=500, null=True)

        class Meta:
                managed = True
                db_table = 'users'
        
        def __str__(self):
                return self.username

