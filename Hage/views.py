from django.shortcuts import render # type: ignore

# Create your views here.

def mostrar(request):
    return render(request, 'index.html')

def catalogo(request):
    return render(request, 'productos.html')

def nosotros(request):
    return render(request, 'nosotros.html')

def contacto(request):
    return render(request, 'contacto.html')

"""producto = get_object_or_404(Producto, id=id)
    perfil = request.session.get('perfil')
    
    carritos_activos = Carrito.objects.filter(usuario=request.user, activo=True)
    
    if carritos_activos.exists():
        carrito = carritos_activos.first()
    else:
        carrito = Carrito.objects.create(usuario=request.user)
    
    detalle_carrito = DetalleCarrito.objects.create(
        carrito=carrito,
        precio_unitario=producto.precio_normal
    )
    
    detalle_carrito.productos.add(producto)
    
    return redirect('inicio')
    
    def ver_carrito(request):
    try:
        carrito = Carrito.objects.get(usuario=request.user, activo=True)
        
        for detalle in carrito.detalles.all():
            detalle.subtotal = detalle.productos.first().precio_final() * detalle.cantidad
            detalle.save()
            
        total_venta = carrito.detalles.all().aggregate(Sum('subtotal'))['subtotal__sum']
    except Carrito.DoesNotExist:
        carrito = None
        total_venta = 0
    
    perfil = request.session.get('perfil') 
    
    context = {
        'carrito': carrito,
        'perfil': perfil,
        'total_venta': total_venta,
    }
    
    return render(request, 'store/cart.html', context)

@login_required
@role_required('admin', 'cliente')
def eliminar_producto_carrito(request, id):
    detalle = get_object_or_404(DetalleCarrito, id=id)
    detalle.delete()
    
    return redirect('ver_carrito')

    """