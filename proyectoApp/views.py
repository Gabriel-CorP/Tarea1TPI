from django.shortcuts import render
import sweetify

# Create your views here.
def index(request):
	return render(request,"index.html")

def pcli(request):
	return render(request,"consola.html")