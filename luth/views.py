from django.shortcuts import render
from django.http import HttpResponse

def index(request):

	context = {'mssg': "luther ncube 22"}

	return render(request, 'index.html', context)
