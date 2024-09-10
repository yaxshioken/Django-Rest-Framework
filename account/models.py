from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.text import slugify
from drf_yasg.openapi import Response
from rest_framework import status
from rest_framework.decorators import action



class User(AbstractUser):
    phone = models.CharField(max_length=13, unique=True)
    email = models.EmailField(unique=True)
    interests = models.ManyToManyField("Interest", related_name="interests")

    def __str__(self):
        return self.username


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=200)
    passport_number = models.CharField(max_length=7)
    passport_letter = models.CharField(max_length=2)

    def __str__(self):
        return self.city


class Interest(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, null=True, blank=True)

    def save(
        self,
        *args,
        force_insert=False,
        force_update=False,
        using=None,
        update_fields=None
    ):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(
            *args,
            force_insert=force_insert,
            force_update=force_update,
            using=using,
            update_fields=update_fields
        )

    def __str__(self):
        return self.name
