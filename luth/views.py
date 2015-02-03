from django.shortcuts import render
from django.http import HttpResponse
from luth.models import Contact

def index(request):

	contact = Contact.objects.all()
	context = {'contacts': contact}

	return render(request, 'index.html', context)
