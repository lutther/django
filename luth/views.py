from django.shortcuts import render
from django.http import HttpResponse
from luth.models import Province, Business

def index(request):

	province = Province.objects.all()
	bns = Business.objects.all()
	context = {'prov': province,
				'bus': bns}

	return render(request, 'index.html', context)
