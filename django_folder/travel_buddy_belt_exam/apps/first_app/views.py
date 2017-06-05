from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.contrib.messages import get_messages
from django.contrib import messages
import re, bcrypt # pip install setuptools # pip install cryptography # pip install bcrypt

def index(request):
	return render(request, 'first_app/index.html')


def travels(request):
	if request.method == "POST":
		post_data = {
        	'name':request.POST['name'],
			'password':request.POST['password'],
			'confirm_password':request.POST['confirm']
		}
		register_result = User.objects.register(post_data)
		print register_result
		if register_result['result'] == "failed_validation":
		    if 'messages' in register_result.keys():
		        for message in register_result['messages']:
		            messages.error(request, message)
		    return redirect('/')
		else:
		    if 'user' in register_result.keys():
		        request.session['current_user'] = register_result['user'].id
		        if 'messages' in register_result.keys():
		            for message in register_result['messages']:
		                messages.success(request, message)
		    else:
		        messages.error(request, "Something went wrong")
		        return redirect('/')
		    return redirect('/')
		return redirect('/')
	return render(request, 'first_app/travels.html')

def destination_seven(request):
	return render(request, 'first_app/destination_seven.html')

def add(request):
	return render(request, 'first_app/add.html')