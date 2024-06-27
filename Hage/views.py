from django.shortcuts import render # type: ignore

# Create your views here.

def mostrar(request):
    return render(request, 'index.html')

def catalogo(request):
    return render(request, 'productos.html')