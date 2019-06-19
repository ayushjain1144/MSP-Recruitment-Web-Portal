from django.db import models

from django.utils import timezone
from django.db.models.signals import post_save
from django.contrib.auth.models import User
class Candidate(models.Model):
    firstname = models.CharField(max_length=25)
    lastname = models.CharField(max_length=25)
    email = models.URLField(default='')
    bitsid = models.CharField(max_length=20)
    contact = models.IntegerField(default=0,min_length=10,max_length=10)

    def update_user_profile(sender, instance, created, **kwargs):
   	    if created:
            Candidate.objects.create(user=instance)
    	    instance.Candidate.save()

# Create your models here.
