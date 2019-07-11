from django.shortcuts import render, HttpResponse, redirect
from .models import Candidate
from django.contrib import auth
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from .forms import PostForm
from .models import Question
from .models import Response
from .forms import GetResponse
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# Create your views here.

#In progress
def login(request):
	if request.user.is_authenticated:
		return redirect(question_list, id = request.user.username)

	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = auth.authenticate(username=username, password=password)

		# correct username and password login the user
		if user is not None:
			auth.login(request, user)
			return redirect(question_list, id = username)

		else:
			messages.error(request, 'Error wrong username/password')

	return render(request, 'test_portal/login.html')


def logout(request):
	auth.logout(request)
	return render(request, 'test_portal/logout.html')


def register(request):
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
			candidate.username = form.cleaned_data['username']
			candidate.password = form.cleaned_data['password']
			candidate.email = form.cleaned_data['email']
			candidate.bitsid = form.cleaned_data['bitsid']
			candidate.contact = form.cleaned_data['contact']
			candidate.save()
			return redirect('test_login')
		else:
			print()
	else:
		form = PostForm()
	return render(request, 'test_portal/register.html', {'form': form})


def question_list(request, pk = Question.objects.order_by("id").values_list('id', flat=True).first(), id = 'a'):
	if not request.user.is_authenticated:
		return redirect('test_login')


	base_pk = Question.objects.order_by("id").values_list('id', flat=True).first()
	questions= Question.objects.order_by("id").all()
	paginator = Paginator(questions, 1)

	page = pk-base_pk + 1

	try:
		questions = paginator.page(page)
	except PageNotAnInteger:
		questions = paginator.page(1)
	except EmptyPage:
		questions = paginator.page(paginator.num_pages)

	try:
		user = Candidate.objects.get(username=id)
		new = Response.objects.get(user=user, question=Question.objects.get(pk = pk))
		form = GetResponse(initial={'free_response': new.free_response})
	except Response.DoesNotExist:
		form = GetResponse(initial={'free_response': 'Answer here!'})

	return render(request, 'test_portal/round2_home.html',{'questions': questions, 'form': form, 'pksent': pk, 'id':id})


def welcome(request):
	return render(request,'test_portal/welcome.html')


def response_save(request, pk, id = 'a'):
	if request.method == 'POST':
		try:
			response = Response.objects.get(user=Candidate.objects.get(username=id), question=Question.objects.get(pk = pk))
		except Response.DoesNotExist:
			response = Response()
		response_rec = GetResponse(request.POST)
		if response_rec.is_valid():
			response.free_response = response_rec.cleaned_data['free_response']
			response.question = Question.objects.get(pk = pk)
			response.user = Candidate.objects.get(username=id)
			response.save()
			if 'SavePrevious' in request.POST:
				pkprev = Question.objects.filter(pk__lt = pk).order_by('-pk').values_list('id', flat=True).first()
				pk = pkprev
				redirect('question_list', pk = pk, id = id)

			elif 'SaveNext' in request.POST:
				pknext = Question.objects.filter(pk__gt = pk).order_by('pk').values_list('id', flat=True).first()
				pk = pknext
				redirect('question_list', pk = pk, id = id)

			else:
				redirect('question_list', pk = pk, id = id)

	else:
		return HttpResponse('You are not supposed to be here! Go Back! Please!')

	return redirect(question_list, pk = pk, id = id)