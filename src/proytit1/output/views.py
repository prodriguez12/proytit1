from django.shortcuts import render, redirect

# Create your views here.
def output_single_view(request, output_id):
	#return  HttpResponse("<h1>Entrega Sprint 2</h1>")
	obj = Output.objects.get(id=output_id)
	context = {
		"titulo": "Output " + str(obj.id),
		"output": obj,

	}
	return render(request, "Output/view.html", context)
def output_list_view(request, *args, **kwargs):
	#return  HttpResponse("<h1>Entrega Sprint 2</h1>")
	lista = Output.objects.all()
	print(lista)
	context = {
		"titulo": "Listado de Outputs",
		"lista": lista
	}
	return render(request, "Output/list.html", context)