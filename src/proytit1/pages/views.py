from django.http import HttpResponse
from django.shortcuts import render
from pages.algoritmo import organizador
from output.models import Output
from input.models import Input


# Create your views here.
def home_view(request, *args, **kwargs):
	#return  HttpResponse("<h1>Entrega Sprint 2</h1>")
	context = {
		"titulo": "Homepage"
	}
	return render(request, "home.html", context)

def apply_view(request, input_id):
	root_file = Input.objects.get(id=input_id).root
	desc = "salida de "+ root_file.name
	new_output = Output(description = desc)
	organizador(root_file.name, 'pages/salida.txt')
	new_output.save_file()
	lista = Output.objects.all()
	context = {
		"titulo": "Listado de Outputs",
		"lista": lista
	}

	return render(request, "Output/list.html", context)