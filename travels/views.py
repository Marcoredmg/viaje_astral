from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Travel
from django.template import loader


def hello_world(request):
	travel = Travel.objects.order_by('id')
	template = loader.get_template('index.html')
	context = {
		'travel': travel
	}
	return HttpResponse(template.render(context, request))

def travel_detail(request, pk):
	travel = get_object_or_404(Travel, pk=pk)
	template = loader.get_template('travel_detail.html')
	context = {
		'travel': travel
	}
	return HttpResponse(template.render(context, request))