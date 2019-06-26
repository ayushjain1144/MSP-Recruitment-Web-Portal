from django.shortcuts import render, HttpResponse, redirect
from .models import Candidate
from django.contrib.auth import login, authenticate
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from .forms import PostForm
from .models import Question
from .models import Response
from .forms import GetResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# Create your views here.

def question_list(request, id = '1'):

	questions= Question.objects.order_by("-id").all()
	paginator = Paginator(questions, 1)

	page = request.GET.get('page')

	form = GetResponse

	try:
		questions = paginator.page(page)
	except PageNotAnInteger:
		questions = paginator.page(1)
	except EmptyPage:
		questions = paginator.page(paginator.num_pages)

	return render(request, 'test_portal/round2_home.html',{'questions': questions, 'form': form, 'id':id})

def login(request):
	if request.method == 'POST':
		form = PostForm(request.POST)

		if form.is_valid():
			email = form.cleaned_data['email']
			try:
				validate_email(email)
			except ValidationError:
				print("oops! wrong email")
			candidate = Candidate()
			candidate.firstname = form.cleaned_data['firstname']
			candidate.lastname = form.cleaned_data['lastname']
			candidate.email = form.cleaned_data['email']
			candidate.bitsid = form.cleaned_data['bitsid']
			candidate.contact = form.cleaned_data['contact']
			candidate.save()
			return redirect('question_list', id = candidate.bitsid)
	else:
		form = PostForm()
	return render(request, 'test_portal/login.html', {'form': form})

def welcome(request):
	return render(request,'test_portal/welcome.html')

def test1(request):
	return HttpResponse('Test!')



def response_save(request, question_rec, id):
	if request.method == 'POST':
		response_rec = GetResponse(request.POST)
		if response_rec.is_valid():
			response = Response()
			response.free_response = response_rec.cleaned_data['free_response']
			response.question = question_rec
			response.user = Candidate.objects.get(id=id)
			response.save()
	else:
		response_rec = GetResponse()

	return render(question_list, id, response_rec)