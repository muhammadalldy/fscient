# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Mahasiswa(models.Model):
    created 		= models.DateTimeField(auto_now_add=True)
    nama	 		= models.CharField(max_length=100, blank=True, default='')
    angkatan        = models.CharField(max_length=100, blank=True, default='')
    noreg           = models.CharField(max_length=100, blank=True, default='')
    peminatan       = models.CharField(max_length=100, blank=True, default='')

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return self.nama

class Profile(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    user 	= models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    email_address = models.EmailField()
    noreg = models.CharField(max_length=100, blank=True)
    angkatan = models.CharField(max_length=100, blank=True)
    peminatan = models.CharField(max_length=100, blank=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return self.user



@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()






class Document(models.Model):
    created         = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='ebook/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self. document


class Journal(models.Model):
    created         = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=255, blank=True)
    journal = models.FileField(upload_to='journal/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.journal







