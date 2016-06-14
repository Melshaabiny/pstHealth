from django.shortcuts import render

# Create your views here.

def renderFit(request):
	return render(request, 'fitness/fitness.html', {})