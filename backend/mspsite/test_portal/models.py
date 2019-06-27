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
	bitsid = models.CharField(max_length=20, unique = True)
	contact = models.IntegerField(default=0,validators=[MinValueValidator(100000000),MaxValueValidator(9999999999)])
	use_required_attribute = True

	def update_user_profile(sender, instance, created, **kwargs):
		if created:
			Candidate.objects.create(user=instance)
			instance.Candidate.save()

	def __str__(self):
		return self.bitsid

# Create your models here.


class Question(models.Model):

	question = models.CharField(max_length=256)
	is_published = models.BooleanField(default = False)

	def __str__(self):
		return self.question


class Answer(models.Model):

	question = models.ForeignKey("Question", related_name = "answer", on_delete=models.DO_NOTHING)
	text = models.CharField(max_length = 1000)

	def __str__(self):
		return self.text


class Response(models.Model):

	user = models.ForeignKey("Candidate", on_delete=models.DO_NOTHING,)
	question = models.ForeignKey("Question", on_delete=models.DO_NOTHING,)

	free_response = models.TextField(max_length = 2000, blank = True)

	def submit(self):
		self.save()

	def __str__(self):
		return self.free_response
