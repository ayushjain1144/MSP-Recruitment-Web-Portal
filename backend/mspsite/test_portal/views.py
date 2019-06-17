from django.shortcuts import render, HttpResponse


# Create your views here.
def login(request):
	return render(request,'test_portal/login.html')
def welcome(request):
	return render(request,'test_portal/welcome.html')
def test(request):
	return HttpResponse('Test!')