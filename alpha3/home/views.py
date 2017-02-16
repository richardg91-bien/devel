from django.shortcuts import render
from django.contrib.auth.views import login

# Create your views here.

from django.shortcuts import render_to_response
from django.template import RequestContext
 
def index(request):
    if request.user.is_authenticated():
	return render(request, 'inmo/index.html')
    else:
	return render(request, 'inmo/login.html')
