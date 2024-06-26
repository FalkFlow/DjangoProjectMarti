from django.db import models

# Create your models here.
def usuarios(Model):
    name = models.CharField(max_length=100, UniqueKey=True)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    slug = models.SlugField(name)
    
    def __str__(self):
        return self.name


def subcategorias(Model):
    name = models.CharField(max_length=100)
    categoria = models.ForeignKey('categorias', on_delete=models.CASCADE)
    slug = models.SlugField(name)
    activate = models.BooleanField()
    
    def __str__(self):
        return self.name
    

def categorias(Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(name)
    activate = models.BooleanField() # En caso de que la categoria no este disponible
    
    def __str__(self):
        return self.name
    
    
def productos(Model):
    name = models.CharField(max_length=100)
    subcategoria = models.ForeignKey('subcategorias', on_delete=models.CASCADE)
    precio = models.FloatField()
    imagen = models.CharField(max_length=1000) # Guardar imagen en nube y guardar url
    slug = models.SlugField(name)
    activate = models.BooleanField() # En caso de que el producto no este disponible
    destacado = models.BooleanField() # Mostrar en la pagina principal
    
    def __str__(self):
        return self.name
    
def carrito(Model):
    usuario = models.ForeignKey('usuarios', on_delete=models.CASCADE)
    producto = models.ForeignKey('productos', on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    slug = models.SlugField(producto.name)
    
    def __str__(self):
        return self.cantidad + ' ' + self.producto.name

