from django.shortcuts import render, HttpResponse

# Create your views here.

def view1(request):
	response = "Hello World!!"
	return HttpResponse(response)
