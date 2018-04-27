from django.shortcuts import render_to_response
from django.http import HttpResponse
# Create your views here.
from .models import Uname,Gender,Birth,Introduction

def index(request):
	name = Uname.objects.all()
	return render_to_response('cms/information.html', locals())