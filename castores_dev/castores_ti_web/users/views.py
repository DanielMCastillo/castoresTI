# home/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import LoginForm
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render
from django.contrib.auth.models import Group
from django.contrib.auth.models import User, Group
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('lista_productos.html')  # O cualquier vista a la que quieras redirigir después de logearse
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Form is not valid.")
    else:
        form = LoginForm()
    
    return render(request, 'home/login.html', {'form': form})



@login_required
@permission_required('productos.add_producto', raise_exception=True)
def agregar_producto(request):
    return render(request, 'productos/agregar_producto.html')

@login_required
def salida_producto(request):
    if request.user.groups.filter(name='Almacenista').exists():
        return render(request, 'productos/salida_producto.html')
    else:
        return render(request, '403.html')  # Página de error si no tiene permiso
    
def crear_usuario(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # Guardamos el nuevo usuario
            usuario = form.save(commit=False)

            # Asignar superuser o staff según el grupo seleccionado
            grupo = request.POST.get('grupo')
            
            if grupo == 'Administrador':
                usuario.is_superuser = True
                usuario.is_staff = True
            elif grupo == 'Almacenista':
                usuario.is_staff = True
                usuario.is_superuser = False

            usuario.save()

            # Asignamos el grupo al usuario
            grupo_obj = Group.objects.get(name=grupo)
            usuario.groups.add(grupo_obj)
            
            messages.success(request, f"Usuario {usuario.username} creado correctamente.")
            return redirect('listar_usuarios')  # Redirigir a la lista de usuarios

    else:
        form = UserCreationForm()

    return render(request, 'crear_usuario.html', {'form': form})

    return render(request, 'crear_usuario.html', {'form': form})

# Vista para listar los usuarios existentes
def listar_usuarios(request):
    usuarios = User.objects.all()
    return render(request, 'listar_usuarios.html', {'usuarios': usuarios})



def mi_vista(request):
    # Obtener los IDs de los grupos
    admin_group_id = 1  # ID del grupo "Administrador"
    almacenista_group_id = 2  # ID del grupo "Almacenista"

    # Verificar si el usuario pertenece a esos grupos según el ID
    es_admin = request.user.groups.filter(id=admin_group_id).exists()
    es_almacenista = request.user.groups.filter(id=almacenista_group_id).exists()

    context = {
        'es_admin': es_admin,
        'es_almacenista': es_almacenista,
    }

    return render(request, 'base.html', context)