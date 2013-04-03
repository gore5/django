# Create your views here.

from django.http import HttpResponse, Http404
from django.template import Context
from django.template.loader import get_template
from django.contrib.auth.models import User

def mainpage(request, username):
	try:
		user = User.objects.get(username=username)
	except:
		raise Http404('User not found.')


	sobres = user.sobre_set.all()
	template = get_template('userpage.html')
	variables = Context({
		'username': username,
		'sobres': sobres
		})
	output = template.render(variables)
	return HttpResponse(output)
