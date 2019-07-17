from django.shortcuts import render, HttpResponse, redirect
from .models import Candidate, Questionm, Questioni, Responsem, Responsei
from django.contrib import auth
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from .forms import PostForm
from .models import Question, Questioni, Questionm
from .models import Response, Responsei, Responsem
from .forms import GetResponse, GetResponsem, GetResponsei
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
			candidate = Candidate()
			candidate.firstname = form.cleaned_data['firstname']
			candidate.lastname = form.cleaned_data['lastname']
			candidate.username = form.cleaned_data['username']
			candidate.password = form.cleaned_data['password']
			candidate.email = form.cleaned_data['email']
			candidate.bitsid = form.cleaned_data['bitsid']
			candidate.contact = form.cleaned_data['contact']
			candidate.description = form.cleaned_data['description']
			candidate.save()
			return redirect('test_login')
		else:
			return HttpResponse(form.errors)
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
		answer = new.free_response
	except Response.DoesNotExist:
		answer = ''
		form = GetResponse(initial={'free_response': 'Answer here!'})

	return render(request, 'test_portal/round2_home.html',{'questions': questions, 'form': form, 'pksent': pk, 'id':id, 'response':answer})


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

			elif 'Finish' in request.POST:
				return redirect('test_logout')

			else:
				redirect('question_list', pk = pk, id = id)

	else:
		return HttpResponse('You are not supposed to be here! Go Back! Please!')

	return redirect(question_list, pk = pk, id = id)

def response_savem(request, pk, id = 'a'):
	if request.method == 'POST':
		try:
			response = Responsem.objects.get(user=Candidate.objects.get(username=id), question=Questionm.objects.get(pk = pk))
		except Responsem.DoesNotExist:
			response = Responsem()
		response_rec = GetResponsem(request.POST)
		if response_rec.is_valid():
			response.responsem = response_rec.cleaned_data['responsem']
			response.question = Questionm.objects.get(pk = pk)
			response.user = Candidate.objects.get(username=id)
			response.save()
			redirect('ques_detail', pk = pk, id = id)

	else:
		return HttpResponse('You are not supposed to be here! Go Back! Please!')

	return redirect(ques_detail, pk = pk, id = id)
def response_savei(request, pk, id = 'a'):
	if request.method == 'POST':
		try:
			response = Responsei.objects.get(user=Candidate.objects.get(username=id), question=Questionm.objects.get(pk = pk))
		except Responsei.DoesNotExist:
			response = Responsei()
		response_rec = GetResponsei(request.POST)
		if response_rec.is_valid():
			response.responsei = response_rec.cleaned_data['responsei']
			response.question = Questioni.objects.get(pk = pk)
			response.user = Candidate.objects.get(username=id)
			response.save()
			redirect('ques_detail2', pk = pk, id = id)

	else:
		return HttpResponse('You are not supposed to be here! Go Back! Please!')

	return redirect(ques_detail2, pk = pk, id = id)


def ques_detail(request, pk, id = 'a'):
	questions= Questionm.objects.order_by("id").all()
	paginator = Paginator(questions, 1)

	page = request.GET.get('page')
	try:
		questions = paginator.page(page)
	except PageNotAnInteger:
		questions = paginator.page(pk)
	except EmptyPage:
		questions = paginator.page(paginator.num_pages)



	try:
		user = Candidate.objects.get(username=id)
		new = Responsem.objects.get(user=user, question=Questionm.objects.get(pk = pk))
		form = GetResponsem(initial={'responsem': new.responsem})
	except Responsem.DoesNotExist:
		form = GetResponsem()

	return render(request, 'test_portal/ques_detail.html',{'questions': questions, 'form':form, 'pksent': pk, 'id':id})


def ques_detail2(request, pk):
	questions= Questioni.objects.order_by("id").all()
	paginator = Paginator(questions, 1)

	page = request.GET.get('page')

	try:
		questions = paginator.page(page)
	except PageNotAnInteger:
		questions = paginator.page(pk)
	except EmptyPage:
		questions = paginator.page(paginator.num_pages)
	new = Responsei.objects.get(user=user, question=Questioni.objects.get(pk = pk))
	form = GetResponsei(initial={'responsei': new.responsei})
	return render(request, 'test_portal/ques_detail2.html',{'questions': questions, 'form':form, 'pksent': pk, 'id':id})

def round2(request):  
	return render(request,'events/round2.html')

def proceed(request):
	ques = Questioni.objects.first()
	context = {'ques': ques}  
	return render(request,'test_portal/proceed.html',context)

def instructions(request):
	ques = Questionm.objects.first()
	context = {'ques': ques}
	return render(request,'test_portal/instructions.html', context)
