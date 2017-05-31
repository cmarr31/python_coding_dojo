from django.conf import settings
from django.shortcuts import render, HttpResponseRedirect
from django.views.decorators.csrf import csrf_protect
import random
import string

@csrf_protect
def index(request):
	attempt = 1
	word = ''.join([random.choice(string.ascii_letters + string.digits) for n in xrange(10)])
	context = {
		"attempts":[
			{"attempt":attempt}
		],
		"words":[
			{"word":word}
		]
	}
	if request.method == 'POST':
		form = ActivateForm( request.POST )
		if form.is_valid():
			actkey = form.cleaned_data['actkey']
			activate( '', actkey )
    		return HttpResponseRedirect('/')
    	else:
			return render(request, 'first_app/index.html', context)

