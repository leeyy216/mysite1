from django.shortcuts import render

# Create your views here.

def bootindex(request):
	return render(request, 'bootstrapindex.html')