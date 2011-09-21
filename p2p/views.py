from django.shortcuts import render_to_response
from bp2p.p2p.models import *
# Create your views here.

def index(request):
	#latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
	return render_to_response('home.html', {'titulo', 'Principal'})

def lista(request):
	m = Medio.objects.all()
	return render_to_response('lista.html', {'medios', m})

