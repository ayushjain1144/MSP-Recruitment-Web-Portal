from django.db import models
from django.conf import settings
from django.utils import timezone
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

class Candidate(models.Model):
	firstname = models.CharField(max_length = 25, default = '')
	lastname = models.CharField(max_length = 25, default = '')
	username = models.CharField(max_length = 25, default = '', unique = True)
	password = models.CharField(max_length =25, default = '')
	email = models.URLField(default = '')
	bitsid = models.CharField(max_length = 20, unique = True)
	contact = models.CharField(max_length = 10, default = '')
	description = models.CharField(max_length = 1000, default = '')
	use_required_attribute = True

	def update_user_profile(sender, instance, created, **kwargs):
		if created:
			Candidate.objects.create(user=instance)
			instance.Candidate.save()

	def __str__(self):
		return self.bitsid

class Question(models.Model):

	question = models.CharField(max_length=256, default = '')
	marks = models.IntegerField(default = 10)
	id = models.AutoField(primary_key = True)

	def __str__(self):
		return self.question


class Response(models.Model):

	user = models.ForeignKey("Candidate", on_delete=models.CASCADE,)
	question = models.ForeignKey("Question", on_delete=models.CASCADE,)

	free_response = models.TextField(max_length = 2000, blank = True)

	def submit(self):
		self.save()

	def __str__(self):
		return self.free_response
