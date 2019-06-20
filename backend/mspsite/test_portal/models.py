from django.db import models
from django.conf import settings
from django.utils import timezone
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

class Candidate(models.Model):
	firstname = models.CharField(max_length=25)
	lastname = models.CharField(max_length=25)
	email = models.URLField(default='')
	bitsid = models.CharField(max_length=20)
	contact = models.IntegerField(default=0,validators=[MinValueValidator(100000000),MaxValueValidator(9999999999)])
	use_required_attribute = True

	def update_user_profile(sender, instance, created, **kwargs):
		if created:
			Candidate.objects.create(user=instance)
			instance.Candidate.save()

# Create your models here.
