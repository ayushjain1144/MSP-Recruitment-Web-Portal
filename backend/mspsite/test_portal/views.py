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
#def login(request):
#	if request.user.is_authenticated:
#		return redirect('admin_page')
#
#	if request.method == 'POST':
#		username = request.POST.get('username')
#		password = request.POST.get('password')
#		user = auth.authenticate(username=username, password=password)
#
#		if user is not None:
#			auth.login(request, user)
#			return redirect('admin_page')
		# correct username and password login the user
#		else:
#			messages.error(request, 'Error wrong username/password')
#
#	return render(request, 'test_portal/login.html')


#def logout(request):
#	auth.logout(request)
#	return render(request, 'test_portal/logout.html')


#def admin_page(request):
#	if not request.user.is_authenticated:
#		return redirect('test_login')

#	return render(request, 'test_portal/admin_page.html')

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
			candidate.email = form.cleaned_data['email']
			candidate.bitsid = form.cleaned_data['bitsid']
			candidate.contact = form.cleaned_data['contact']
			candidate.save()
			return redirect(question_list, pk = 1, id = candidate.bitsid)
		else:
			print()
	else:
		form = PostForm()
	return render(request, 'test_portal/register.html', {'form': form})


def question_list(request, pk, id = 'a'):

	questions= Question.objects.order_by("id").all()
	paginator = Paginator(questions, 1)

	page = request.GET.get('page')

	try:
		questions = paginator.page(page)
	except PageNotAnInteger:
		questions = paginator.page(pk)
	except EmptyPage:
		questions = paginator.page(paginator.num_pages)

	try:
		user = Candidate.objects.get(bitsid=id)
		new = Response.objects.get(user=user, question=questions.object_list.first())
		form = GetResponse(initial={'free_response': new.free_response})
	except Response.DoesNotExist:
		form = GetResponse(initial={'free_response': 'Answer here!'})

	return render(request, 'test_portal/round2_home.html',{'questions': questions, 'form': form, 'pksent': pk, 'id':id})



def welcome(request):
	return render(request,'test_portal/welcome.html')

def test1(request):
	return HttpResponse('Test!')



def response_save(request, pk, id = 'a'):
	if request.method == 'POST':
		try:
			response = Response.objects.get(user=Candidate.objects.get(bitsid=id), question=Question.objects.get(pk = pk))
		except Response.DoesNotExist:
			response = Response()
		response_rec = GetResponse(request.POST)
		if response_rec.is_valid():
			response.free_response = response_rec.cleaned_data['free_response']
			response.question = Question.objects.get(pk = pk)
			response.user = Candidate.objects.get(bitsid=id)
			response.save()
			redirect(question_list, pk = pk, id = id)

	else:
		return HttpResponse('You are not supposed to be here! Go Back! Please!')

	return redirect(question_list, pk = pk, id = id)