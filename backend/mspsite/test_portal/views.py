from django.shortcuts import render, HttpResponse
from .models import Candidate
from django.contrib.auth import login, authenticate
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
# Create your views here.
def login(request):
	if request.method == 'POST':
        	form = Candidate(request.POST)
        	try:
    			validate_email(bitsmail)
		except ValidationError:
    			print "oops! wrong email"
		else:
        		if form.is_valid():
        		form.save()
                	login(request, user)
                	return redirect('test')
    	else:
        	form = Candidate()
    	return render(request, 'test_portal/login.html', {'form': form})
def welcome(request):
	return render(request,'test_portal/welcome.html')
def test(request):
	return HttpResponse('Test!')
