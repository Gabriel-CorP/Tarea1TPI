from django.http.response import JsonResponse
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
import sweetify

# Create your views here.
def index(request):
	return render(request,"index.html")

def pcli(request):
	return render(request,"consola.html")

def arrays(request):
	return render(request,"arrays.html")

def estructuraDatos(request):
    return render(request,"estructuras-de-datos.html")

def arraylist(request):
	return render(request,"arraylist.html")

def queue(request):
	return render(request,"queue.html")

def stack(request):
	return render(request,"stack.html")

def sortedlist(request):
	return render(request,"sortedlist.html")

def programacionWeb(request):
	return render(request, "programacion-web.html")

def baseDeDatos(request):
	return render(request, "base-de-datos.html")

def vistas(request):
	return render(request, "vistas.html")
    

def aspsql(request):
	return render(request, "asp_sqlconection.html")

def POO(request):
	return render(request, "POO.html")

def enviarCorreo(request):
	subject=request.GET.get("asunto")
	messa=request.GET.get("mensaje")
	correousuario=request.GET.get("email")
	print(subject)
	print(messa)
	print(correousuario)
	message=messa+" att: " + correousuario
	email_from=settings.EMAIL_HOST_USER
	recipient_list=["gabrielcorena@gmail.com"]

	contexto={'nose':"nada"}
	send_mail(subject,message,email_from,recipient_list)
	return (JsonResponse(contexto))
