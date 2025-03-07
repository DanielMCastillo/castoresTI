from django.forms import ValidationError
from django.http import HttpResponseForbidden
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Producto, SalidaProducto
from .forms import MovimientoProductoForm, ProductoForm, SalidaProductoForm
from .models import MovimientoProducto
from django.views.generic import ListView

# Vista para agregar productos
def agregar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        
        if form.is_valid():
            # Guardar el producto
            producto = form.save()

            # Crear un movimiento de tipo 'entrada' automáticamente
            MovimientoProducto.objects.create(
                producto=producto,
                tipo_movimiento='entrada',
                cantidad=producto.cantidad,  # O la cantidad ingresada
                realizado_por=request.user  # Usuario actual
            )

            # Redirigir a la lista de productos o cualquier otra vista
            return redirect('lista_productos')
    
    else:
        form = ProductoForm()

    return render(request, 'agregar_producto.html', {'form': form})

# Vista para listar productos
def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'lista_productos.html', {'productos': productos})


def aumentar_inventario(request, producto_id):
    producto = get_object_or_404(Producto, idproducto=producto_id)

    if request.method == "POST":
        cantidad = int(request.POST.get("cantidad", 0))
        
        if cantidad > 0:
            producto.cantidad += cantidad
            producto.save()
            messages.success(request, "Inventario actualizado correctamente.")
        else:
            messages.error(request, "No se puede disminuir el inventario.")

    return redirect('lista_productos')

def cambiar_estatus_producto(request, producto_id):
    producto = get_object_or_404(Producto, idproducto=producto_id)
    
    if producto.estatus == "activo":
        producto.estatus = "inactivo"
        messages.success(request, "Producto dado de baja correctamente.")
    else:
        producto.estatus = "activo"
        messages.success(request, "Producto activado nuevamente.")

    producto.save()
    return redirect('lista_productos')

def lista_productos(request):
    productos_activos = Producto.objects.filter(estatus='activo')
    productos_inactivos = Producto.objects.filter(estatus='inactivo')
    return render(request, 'lista_productos.html', {'productos_activos': productos_activos, 'productos_inactivos': productos_inactivos})
def salida_producto(request):
    if request.method == 'POST':
        form = SalidaProductoForm(request.POST)
        if form.is_valid():
            try:
                # Obtener el producto y la cantidad de salida
                producto = form.cleaned_data['producto']
                cantidad_salida = form.cleaned_data['cantidad_salida']
                
                # Verificar si hay suficiente inventario
                if cantidad_salida > producto.cantidad:
                    raise ValidationError(f"No hay suficiente inventario. Solo hay {producto.cantidad} unidades disponibles.")
                
                # Actualizar el inventario
                producto.cantidad -= cantidad_salida
                producto.save()

                # Mensaje de éxito
                messages.success(request, f"Salida de producto realizada correctamente. Quedan {producto.cantidad} unidades en inventario.")
                return redirect('lista_productos')  # Redirige a la lista de productos

            except ValidationError as e:
                # Si ocurre un error de validación, mostrarlo
                messages.error(request, str(e))
                return render(request, 'salida_producto.html', {'form': form})
        else:
            # Si el formulario no es válido, volver a mostrarlo con los errores
            return render(request, 'salida_producto.html', {'form': form})
    else:
        # Crear un formulario vacío cuando la solicitud es GET
        form = SalidaProductoForm()

    return render(request, 'salida_producto.html', {'form': form})

def registrar_movimiento(request):
    if request.method == 'POST':
        form = MovimientoProductoForm(request.POST)
        if form.is_valid():
            movimiento = form.save(commit=False)
            movimiento.realizado_por = request.user  # Asignamos el usuario que está realizando el movimiento
            movimiento.save()
            return redirect('listar_movimientos')  # Redirigir a la lista de movimientos
    else:
        form = MovimientoProductoForm()

    return render(request, 'registro_movimiento.html', {'form': form})

def listar_movimientos(request):
    # Obtener el tipo de movimiento filtrado (por ejemplo, 'entrada' o 'salida')
    tipo_movimiento = request.GET.get('tipo_movimiento', None)

    if tipo_movimiento:
        movimientos = MovimientoProducto.objects.filter(tipo_movimiento=tipo_movimiento)
    else:
        movimientos = MovimientoProducto.objects.all()

    return render(request, 'listar_movimientos.html', {'movimientos': movimientos})


def mi_vista_admin(request):
    if not request.user.is_superuser:
        return HttpResponseForbidden("No tienes permisos para acceder a esta página.")
    
    # El resto de la lógica de la vista para administradores
    return render(request, 'admin_dashboard.html')