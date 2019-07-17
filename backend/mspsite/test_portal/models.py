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
class Responsei(models.Model):

	user = models.ForeignKey("Candidate", on_delete=models.CASCADE,)
	question = models.ForeignKey("Questioni", on_delete=models.CASCADE,)

	responsei = models.IntegerField(default = 10)

	def submit(self):
		self.save()

	def __str__(self):
		return self.responsei
	
class Responsem(models.Model):

	user = models.ForeignKey("Candidate", on_delete=models.CASCADE,)
	question = models.ForeignKey("Questionm", on_delete=models.CASCADE,)

	responsem1 = models.BooleanField()
	responsem2 = models.BooleanField()
	responsem3 = models.BooleanField()
	responsem4 = models.BooleanField()

	def submit(self):
		self.save()

	def __str__(self):
		return self.responsem
	
class Questionm(models.Model):

	question = models.TextField()
	opt1 = models.CharField(default='', max_length=200)
	opt2 = models.CharField(default='', max_length=200)
	opt3 = models.CharField(default='', max_length=200)
	opt4 = models.CharField(default='', max_length=200)
	marks = models.IntegerField(default = 10)

	def __str__(self):
		return self.question

	def publish(self):
		self.published_date = timezone.now()
		self.save()

class Questioni(models.Model):

	question = models.TextField()
	marks = models.IntegerField(default = 10)

	def __str__(self):
		return self.question

	def publish(self):
		self.published_date = timezone.now()
		self.save()
