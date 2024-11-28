from django.shortcuts import render, redirect, get_object_or_404
from aplicacion.forms import FormProducto, FormProveedor, FormTienda
from django.contrib import messages
from aplicacion.models import Producto, Proveedor, Tienda

# Página de inicio
def index(request):
    return render(request, 'templatesApp/index.html')

# Listado de productos
def listado_productos(request):
    productos = Producto.objects.all()
    return render(request, 'templatesApp/lista_productos.html', {'productos': productos})

# Agregar un producto
def agregar_producto(request):
    form = FormProducto()
    if request.method == 'POST':
        form = FormProducto(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "El producto ha sido agregado exitosamente.")
            return redirect('listado_productos')
    return render(request, 'templatesApp/agregar_producto.html', {'form': form})

# Eliminar un producto
def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    producto.delete()
    messages.success(request, f"El producto '{producto.nombre}' ha sido eliminado exitosamente.")
    return redirect('listado_productos')

# Actualizar un producto
def actualizar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    form = FormProducto(instance=producto)
    if request.method == 'POST':
        form = FormProducto(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            messages.success(request, "El producto ha sido actualizado exitosamente.")
            return redirect('listado_productos')
    return render(request, 'templatesApp/agregar_producto.html', {'form': form})

# Listado de proveedores
def listado_proveedores(request):
    proveedores = Proveedor.objects.all()
    return render(request, 'templatesApp/lista_proveedor.html', {'proveedores': proveedores})

# Agregar un proveedor
def agregar_proveedor(request):
    form = FormProveedor()
    if request.method == 'POST':
        form = FormProveedor(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "El proveedor ha sido registrado exitosamente.")
            return redirect('listado_proveedores')
    return render(request, 'templatesApp/agregar_proveedor.html', {'form': form})

# Eliminar un proveedor
def eliminar_proveedor(request, id):
    proveedor = get_object_or_404(Proveedor, id=id)
    proveedor.delete()
    messages.success(request, f"El proveedor '{proveedor.nombre}' ha sido eliminado exitosamente.")
    return redirect('listado_proveedores')

# Actualizar un proveedor
def actualizar_proveedor(request, id):
    proveedor = get_object_or_404(Proveedor, id=id)
    form = FormProveedor(instance=proveedor)
    if request.method == 'POST':
        form = FormProveedor(request.POST, instance=proveedor)
        if form.is_valid():
            form.save()
            messages.success(request, "El proveedor ha sido actualizado exitosamente.")
            return redirect('listado_proveedores')
    return render(request, 'templatesApp/agregar_proveedor.html', {'form': form})

# Listado de tiendas
def listado_tiendas(request):
    tiendas = Tienda.objects.all()
    return render(request, 'templatesApp/lista_tiendas.html', {'tiendas': tiendas})

# Agregar una tienda
def agregar_tiendas(request):
    form = FormTienda()
    if request.method == 'POST':
        form = FormTienda(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "La tienda ha sido registrada exitosamente.")
            return redirect('listado_tiendas')
    return render(request, 'templatesApp/agregar_tienda.html', {'form': form})

# Eliminar una tienda
def eliminar_tienda(request, id):
    tienda = get_object_or_404(Tienda, id=id)
    tienda.delete()
    messages.success(request, f"La tienda '{tienda.nombre}' ha sido eliminada exitosamente.")
    return redirect('listado_tiendas')

# Actualizar una tienda
def actualizar_tienda(request, id):
    tienda = get_object_or_404(Tienda, id=id)
    form = FormTienda(instance=tienda)
    if request.method == 'POST':
        form = FormTienda(request.POST, instance=tienda)
        if form.is_valid():
            form.save()
            messages.success(request, "La tienda ha sido actualizada exitosamente.")
            return redirect('listado_tiendas')
    return render(request, 'templatesApp/agregar_tienda.html', {'form': form})

