from django.db import models
from django.conf import settings
from django.utils import timezone
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator



class Exam(models.Model):
	user = models.ForeignKey("Candidate", on_delete=models.CASCADE,)
	duration = models.IntegerField(default = 60)
	start_time = models.DateTimeField()


class Candidate(models.Model):
	firstName = models.CharField(max_length = 25, default = '')
	lastName = models.CharField(max_length = 25, default = '')
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
	
class QuestionSub(models.Model):

	question = models.CharField(max_length=256, default = '')
	marks = models.IntegerField(default = 10)
	ques_no = models.IntegerField(null = True)

	def __str__(self):
		return self.question

class QuestionMCQ(models.Model):

	question = models.CharField(max_length=256, default = '')
	opt1 = models.CharField(default='', max_length=200)
	opt2 = models.CharField(default='', max_length=200)
	opt3 = models.CharField(default='', max_length=200)
	opt4 = models.CharField(default='', max_length=200)
	marks = models.IntegerField(default = 10)
	ques_no = models.IntegerField(null=True)

	def __str__(self):
		return self.question

class ResponseSub(models.Model):

	user = models.ForeignKey("Candidate", on_delete=models.CASCADE,)
	question = models.ForeignKey("QuestionSub", on_delete=models.CASCADE,)

	free_response = models.TextField(max_length = 2000, blank = True)

	def submit(self):
		self.save()

	def __str__(self):
		return self.free_response
	
class ResponseMCQ(models.Model):

	user = models.ForeignKey("Candidate", on_delete=models.CASCADE,)
	question = models.ForeignKey("QuestionMCQ", on_delete=models.CASCADE,)

	response1 = models.BooleanField(default=False)
	response2 = models.BooleanField(default=False)
	response3 = models.BooleanField(default=False)
	response4 = models.BooleanField(default=False)

	def submit(self):
		self.save()

	def __str__(self):
		return str(self.response1)
	
