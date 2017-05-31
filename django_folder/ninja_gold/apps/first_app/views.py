from django.shortcuts import render, HttpResponse
from django import forms
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_protect
import random


@csrf_protect
def index(request):
	your_gold = 0
	ten_20 = random.randint(10,20)
	five_10 = random.randint(5,10)
	two_5 = random.randint(2,5)
	zero_50 = random.randint(0,50)
	context = {
		"golds":[
			{"your_gold":your_gold},
			{"ten_20":ten_20},
			{"five_10":five_10},
			{"two_5":two_5},
			{"zero_50":zero_50}
		]
	}
	return render(request, 'first_app/index.html', context)

@csrf_protect
def process_money(request):
	return HttpResponseRedirect('/')