from django.shortcuts import render, HttpResponse

# Create your views here.

def doesnt_matter(request):
	response = "I did it!!!!"
	return HttpResponse(response)