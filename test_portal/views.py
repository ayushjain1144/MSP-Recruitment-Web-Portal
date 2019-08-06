from django.shortcuts import render, HttpResponse, redirect
from .models import Candidate
from django.contrib import auth
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from .forms import PostForm
from .models import QuestionSub, QuestionMCQ
from .models import ResponseSub, ResponseMCQ, Exam
from .forms import GetResponse, GetResponseMCQ
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.utils import timezone

# Create your views here.

def welcome(request):
	return render(request,'test_portal/welcome.html')

def register(request):
	if request.method == 'POST':
		form = PostForm(request.POST)

		if form.is_valid():
			candidate = Candidate()
			candidate.firstName = form.cleaned_data['firstName']
			candidate.lastName = form.cleaned_data['lastName']
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

def login(request):
	if request.user.is_authenticated:
		return redirect(ques_detail_mcq, id = request.user.username)

	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = auth.authenticate(username=username, password=password)

		# correct username and password login the user
		if user is not None:
			try:
				user1 = Candidate.objects.get(username=username)
				exam = Exam.objects.get(user = user1)
				if exam.logged_out is 1:
					return HttpResponse('You have finished the test')
				else:
					auth.login(request, user)
					return redirect(ques_detail_mcq, id = username)				
			except Exam.DoesNotExist:
				exam = Exam()
				exam.user = Candidate.objects.get(username=username)
				exam.start_time = timezone.now()
				exam.logged_in = 1
				exam.save()
				auth.login(request, user)
				return redirect(ques_detail_mcq, id = username)

		else:
			messages.error(request, 'Error wrong username/password')

	return render(request, 'test_portal/login.html')

def instructions(request):
	ques = QuestionMCQ.objects.first()
	context = {'ques': ques}
	return render(request,'test_portal/instructions.html', context)

def ques_detail_mcq(request, ques_no = 1, id = 'a'):
	if not request.user.is_authenticated:
		return redirect('test_login')

	ques_count= QuestionMCQ.objects.order_by("ques_no").count()

	question = QuestionMCQ.objects.get(ques_no=ques_no)

	user1 = Candidate.objects.get(username=id)
	exam = Exam.objects.get(user = user1)
	time = exam.start_time

	try:
		user = Candidate.objects.get(username=id)
		new = ResponseMCQ.objects.get(user=user, question=QuestionMCQ.objects.get(ques_no = ques_no))
		form = GetResponseMCQ(initial={'response1': new.response1,'response2': new.response2,'response3': new.response3,'response4': new.response4})
		res1 = new.response1
		res2 = new.response2
		res3 = new.response3
		res4 = new.response4
	except ResponseMCQ.DoesNotExist:
		res1 = False
		res2 = False
		res3 = False
		res4 = False
		form = GetResponseMCQ()

	return render(request, 'test_portal/round1.html',{'question': question, 'form': form, 'pksent': ques_no, 'id':id, 'n' : range(1,ques_count+1), 'time' : time,
														   'response1' : res1,'response2' : res2,'response3' : res3, 'response4' : res4, 'count' : ques_count})

def response_savem(request, pk, next, id = 'a'):
	if request.method == 'POST':
		try:
			response = ResponseMCQ.objects.get(user=Candidate.objects.get(username=id), question=QuestionMCQ.objects.get(ques_no = pk))
		except ResponseMCQ.DoesNotExist:
			response = ResponseMCQ()
		response_rec = GetResponseMCQ(request.POST)
		if response_rec.is_valid():
			response.response1 = response_rec.cleaned_data['response1']
			response.response2 = response_rec.cleaned_data['response2']
			response.response3 = response_rec.cleaned_data['response3']
			response.response4 = response_rec.cleaned_data['response4']
			response.question = QuestionMCQ.objects.get(pk = pk)

			if (response.response1 == response.question.ans1) and (response.response2 == response.question.ans2) and (response.response3 == response.question.ans3) and (response.response4 == response.question.ans4):
				response.marks = response.question.marks

			response.user = Candidate.objects.get(username=id)
			response.save()
			if 'SavePrevious' in request.POST:
				next = pk - 1
				return redirect('ques_detail_mcq', ques_no = next, id = id)

			elif 'SaveNext' in request.POST:
				next = pk + 1
				return redirect('ques_detail_mcq', ques_no = next, id = id)

			elif 'Finish' in request.POST:
				user = Candidate.objects.get(username=id)
				exam = Exam.objects.get(user = user)
				exam.logged_out = 1
				exam.save()
				return redirect('test_logout')

			elif 'Round2' in request.POST:
				return redirect(question_list, id = id)

			else:
				next = int(request.POST['progress-number'])
				return redirect('ques_detail_mcq', ques_no = next, id = id)

	else:
		return HttpResponse('You are not supposed to be here! Go Back! Please!')

	return redirect(ques_detail_mcq, ques_no = next, id = id)

def question_list(request, ques_no = 1, id = 'a'):
	if not request.user.is_authenticated:
		return redirect('test_login')

	ques_count= QuestionSub.objects.order_by("ques_no").count()

	question = QuestionSub.objects.get(ques_no=ques_no)

	user1 = Candidate.objects.get(username=id)
	exam = Exam.objects.get(user = user1)
	time = exam.start_time

	try:
		user = Candidate.objects.get(username=id)
		new = ResponseSub.objects.get(user=user, question=QuestionSub.objects.get(ques_no = ques_no))
		form = GetResponse(initial={'free_response': new.free_response})
		answer = new.free_response
	except ResponseSub.DoesNotExist:
		answer = ''
		form = GetResponse(initial={'free_response': 'Answer here!'})


	return render(request, 'test_portal/round2.html',{'question': question, 'form': form, 'time' : time, 'pksent': ques_no, 'id':id, 'n' : range(1,ques_count+1), 'i' : 1, 'response' : answer, 'count' : ques_count})

def response_save(request, pk, next, id = 'a',):
	if request.method == 'POST':
		try:
			response = ResponseSub.objects.get(user=Candidate.objects.get(username=id), question=QuestionSub.objects.get(ques_no = pk))
		except ResponseSub.DoesNotExist:
			response = ResponseSub()
		response_rec = GetResponse(request.POST)
		if response_rec.is_valid():
			response.free_response = response_rec.cleaned_data['free_response']
			response.question = QuestionSub.objects.get(ques_no = pk)
			response.user = Candidate.objects.get(username=id)
			response.save()
			if 'SavePrevious' in request.POST:
				next = pk - 1
				return redirect('question_list', ques_no = next, id = id)

			elif 'SaveNext' in request.POST:
				next = pk + 1
				return redirect('question_list', ques_no = next, id = id)

			elif 'Round1' in request.POST:
				return redirect(ques_detail_mcq, id = id)

			elif 'Finish' in request.POST:
				user = Candidate.objects.get(username=id)
				exam = Exam.objects.get(user = user)
				exam.logged_out = 1
				exam.save()
				return redirect('test_logout')

			else:
				next = int(request.POST['progress-number'])
				return redirect('question_list', ques_no = next, id = id)

	else:
		return HttpResponse('You are not supposed to be here! Go Back! Please!')

	return redirect(question_list, ques_no = next, id = id)

def logout(request):
	auth.logout(request)
	return render(request, 'test_portal/logout.html')
