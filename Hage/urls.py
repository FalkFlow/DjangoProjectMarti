from django.urls import path # type: ignore
from . import views


urlpatterns = [
    path('', views.mostrar, name='index'),
    path('catalogo/', views.catalogo, name='catalogo'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('contacto/', views.contacto, name='contacto'),
]