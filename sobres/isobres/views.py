# Create your views here.

from django.http import HttpResponse, Http404
from django.template import Context
from django.template.loader import get_template
from django.contrib.auth.models import User
from django.shortcuts import render_to_response

def mainpage(request):
	return render_to_response('mainpage.html'{'titlehead': 'Sobres aPP','pagetitle': 'Welcome to the Sobres aPPlication','contentbody': 'Managing non legal funding since 2013','user': request.user })
	
