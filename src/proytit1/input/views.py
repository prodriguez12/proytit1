from django.shortcuts import render, redirect

from .form import InputForm
from .models import Input

# Create your views here.
def input_new_view(request, *args, **kwargs):
	#return  HttpResponse("<h1>Entrega Sprint 2</h1>")
	form = InputForm(request.POST or None, request.FILES)
	if form.is_valid():
		form.save()
		return redirect('/inputs/')
	context = {
		"titulo": "nuevo input",
		"formulario": form
	}
	return render(request, "input/new.html", context)

def input_single_view(request, input_id):
	#return  HttpResponse("<h1>Entrega Sprint 2</h1>")
	obj = Input.objects.get(id=input_id)
	context = {
		"titulo": "Input " + str(obj.id),
		"input": obj,

	}
	return render(request, "input/view.html", context)

def input_list_view(request, *args, **kwargs):
	#return  HttpResponse("<h1>Entrega Sprint 2</h1>")
	lista = Input.objects.all()
	print(lista)
	context = {
		"titulo": "Listado de inputs",
		"lista": lista
	}
	return render(request, "input/list.html", context)