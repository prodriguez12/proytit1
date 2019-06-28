from django.http import HttpResponse
from django.shortcuts import render
#from pages.portage import algoritmo
from output.models import Output
from input.models import Input
from datetime import datetime
import zipfile


# Create your views here.
def home_view(request, *args, **kwargs):
	#return  HttpResponse("<h1>Entrega Sprint 2</h1>")
	context = {
		"titulo": "Homepage"
	}
	return render(request, "home.html", context)

def apply_view(request, input_id):
	inpt = Input.objects.get(id=input_id)
	root = inpt.gbd.path
	start = datetime.now()
	#desc = "salida de "+ root_file.name
	#new_output = Output(description = desc)
	#algoritmo(root,spd_tol,buffr,n_freq,np,input_data)
	#new_output.save_file()
	finish = datetime.now()
	lista = Output.objects.all()
	context = {
		"titulo": "Listado de Outputs",
		"lista": lista
	}

	return render(request, "Output/list.html", context)