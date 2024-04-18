# from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import User 
# from django.conf import settings
# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from rest_framework_simplejwt.tokens import Token

# Create your models here.


# class user(AbstractUser):
#     name = models.CharField(max_length=255,)
#     email = models.CharField(max_length=255,unique=True)
#     password = models.CharField(max_length=255)


#     first_name = None
#     last_name = None
#     username = None

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []


# class refreshstore(models.Model):
#     refresh = models.TextField(max_length=1000,default="",blank=False)
#     user = models.ForeignKey(User , null=True , on_delete=models.CASCADE)


# @receiver(post_save, sender=User)
# def store_token(sender , instance=None , created=False , **kwargs):
#     if created:
#         Token.objects.create(user=instance)


class refreshtoken(models.Model):
    refresh = models.TextField(max_length=1000)
    user = models.ForeignKey(User , null=True , on_delete=models.CASCADE)


    def __str__(self):
        return self.user.username
