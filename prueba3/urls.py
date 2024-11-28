"""Prueba URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from aplicacion import views

from django.contrib import admin
from django.urls import path
from aplicacion import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Página de inicio
    path('', views.index, name='index'),

    # Productos
    path('productos/', views.listado_productos, name='listado_productos'),
    path('productos/agregar/', views.agregar_producto, name='agregar_producto'),
    path('productos/eliminar/<int:id>/', views.eliminar_producto, name='eliminar_producto'),
    path('productos/actualizar/<int:id>/', views.actualizar_producto, name='actualizar_producto'),

    # Proveedores
    path('proveedores/', views.listado_proveedores, name='listado_proveedores'),
    path('proveedores/agregar/', views.agregar_proveedor, name='agregar_proveedor'),
    path('proveedores/eliminar/<int:id>/', views.eliminar_proveedor, name='eliminar_proveedor'),
    path('proveedores/actualizar/<int:id>/', views.actualizar_proveedor, name='actualizar_proveedor'),

    # Tiendas
    path('tiendas/', views.listado_tiendas, name='listado_tiendas'),
    path('tiendas/agregar/', views.agregar_tiendas, name='agregar_tienda'),
    path('tiendas/eliminar/<int:id>/', views.eliminar_tienda, name='eliminar_tienda'),
    path('tiendas/actualizar/<int:id>/', views.actualizar_tienda, name='actualizar_tienda'),
]

