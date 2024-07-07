from django.shortcuts import render, redirect # type: ignore
from .models import * # type: ignore
from .forms import *
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def mostrar(request):
    productos_destacados = productos.objects.filter(destacado=True)
    perfil = request.session.get('perfil')
    context = {'productos': productos_destacados, 'perfil': perfil}
    return render(request, 'index.html', context)


def catalogo(request):
    all_productos = productos.objects.all()
    all_categorias = categorias.objects.all()
    perfil = request.session.get('perfil')
    context = {'productos': all_productos, 'categorias': all_categorias, 'perfil': perfil}
    return render(request, 'productos.html', context)

def nosotros(request):
    perfil = request.session.get('perfil')
    context = {'perfil': perfil}
    return render(request, 'nosotros.html', context)

def contacto(request):
    perfil = request.session.get('perfil')
    context = {'perfil': perfil}
    return render(request, 'contacto.html', context)

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('usuario')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                try:
                    profile = usuarios.objects.get(username=user)
                    request.session['perfil'] = profile.rol
                except usuarios.DoesNotExist:
                    form.add_error(None, 'Perfil no encontrado para el usuario.')
                login(request, user)
                return redirect('index')
            else:
                form.add_error(None, 'Usuario o contraseña incorrectos, intente nuevamente')
    else:
        form = LoginForm()
        
    return render(request, 'login.html', {'form': form})


def registro(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            profile = usuarios.objects.create(username=user, rol='cliente')  
            request.session['perfil'] = 'cliente'  # O el rol que corresponda
            
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'registro.html', {'form': form})

    
def agregar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogo')  
    else:
        form = ProductoForm()
    return render(request, 'añadir_producto.html', {'form': form})

def carrito(request):
    perfil = request.session.get('perfil')
    context = {'perfil': perfil}
    return render(request, 'carrito.html', context)

def pago(request):
    
    perfil = request.session.get('perfil')
    context = {'perfil': perfil}
    return render(request, 'pago.html', context)

