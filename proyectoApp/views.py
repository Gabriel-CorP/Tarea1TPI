from django.shortcuts import render
import sweetify

# Create your views here.
def index(request):
	return render(request,"index.html")

def pcli(request):
	return render(request,"consola.html")

def arrays(request):
	return render(request,"arrays.html")

def arraylist(request):
	return render(request,"arraylist.html")

def sortedlist(request):
	return render(request,"sortedlist.html")