from django.db import models

# Create your models here.
class usuarios(models.Model):
    username = models.CharField(max_length=100) # Nombre de usuario
    name = models.CharField(max_length=100) # Nombre 
    last_name = models.CharField(max_length=100) # Apellido
    email = models.EmailField()
    password = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name


class categorias(models.Model):
    name = models.CharField(max_length=100)
    activate = models.BooleanField() # En caso de que la categoria no este disponible
    
    def __str__(self):
        return self.name
    
    
class productos(models.Model):
    name = models.CharField(max_length=100)
    categoria = models.ForeignKey('categorias', on_delete=models.CASCADE)
    precio = models.FloatField()
    imagen = models.CharField(max_length=1000) # Guardar imagen en nube y guardar url
    activate = models.BooleanField() # En caso de que el producto no este disponible
    destacado = models.BooleanField() # Mostrar en la pagina principal
    
    def __str__(self):
        return self.name
    
class carrito(models.Model):
    usuario = models.ForeignKey('usuarios', on_delete=models.CASCADE)
    producto = models.ForeignKey('productos', on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    
    def __str__(self):
        return self.cantidad + ' ' + self.producto.name

