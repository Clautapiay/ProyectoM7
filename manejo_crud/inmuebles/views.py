from django.shortcuts import render, HttpResponse, HttpResponseRedirect, get_object_or_404
from .models import Inmueble, Perfil, Region, Comuna, Contact
from .forms import UserForm, PerfilForm, InmuebleForm, ContactForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.
# def index(request):
#     return HttpResponse('Hola Mundo')
@login_required(login_url='/login/')
def index(request):
    regiones = Region.objects.all()
    comunas = Comuna.objects.all()
    region_id = request.GET.get('region')
    comuna_id = request.GET.get('comuna')
    inmuebles = Inmueble.objects.all()

    if region_id:
        inmuebles = inmuebles.filter(id_region=region_id)
    if comuna_id:
        inmuebles = inmuebles.filter(id_comuna=comuna_id)

    context = {
        'inmuebles': inmuebles,
        'regiones': regiones,
        'comunas': comunas
    }
    return render(request, 'index.html', context)

def register(request):
    if request.user.is_authenticated: #validamos ... antes de validad el metodo, para que asi no se pueda registrar al tener una sesion iniciada
        return HttpResponseRedirect('/') 
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid(): #se tiene que preguntar por validacion, para ver si es valido o no
            form.save()
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            ultimo_usuario_creado = authenticate(request, username=username, password=password) #creo registro
            #ultimo_usuario_creado = User.objects.last()
            login(request,ultimo_usuario_creado) #inicio sesion
    
            #print(ultimo_usuario_creado.username)
            return HttpResponseRedirect(f'/profile/') #me envia a sesion completa con datos
        context = {'form': form}
        return render(request,'registration/register.html', context)
    else:
        form = UserForm() #se genera instancia vacia
        context = {'form': form}
        return render(request,'registration/register.html', context)

@login_required(login_url='/login/')
def profile(request):
    usuario = request.user
    tipo_de_usuario = Perfil.objects.get(usuario=usuario).tipo_de_usuario.tipo_de_usuario
    perfil = Perfil.objects.filter(usuario=usuario)
    if perfil.exists():
        perfil=perfil[0]
    else:
        perfil = None
    context = {'perfil':perfil,
               'tipo':tipo_de_usuario}
    return render(request, 'profile.html', context)

@login_required(login_url='/login/')
def register_profile(request):
    usuario = request.user #nos traemos un objeto del tipo User, que viene del auth de django
    if request.method == "POST":
        form = PerfilForm(request.POST)
        if form.is_valid():
            usuario = usuario
            tipo = form.cleaned_data['tipo_de_usuario']
            rut = form.cleaned_data['rut']
            direccion = form.cleaned_data['direccion']
            telefono = form.cleaned_data['telefono_personal']
            correo = usuario.email
            
            datos = Perfil(
                usuario=usuario,
                tipo_de_usuario=tipo,
                rut=rut,
                direccion=direccion,
                telefono_personal=telefono,
                correo_electronico=correo
                )
            datos.save()
            return HttpResponseRedirect('/profile/')
        
    else:
        
        #si es que tebemos metodo GET
        form = PerfilForm()
    context = {
        'form':form,
        'title':'Crea tu Perfil'
        }
    return render(request, 'register_profile.html', context)

@login_required(login_url='/login/')
def update_profile(request):
    usuario = request.user  
    print("empiza el if 1")
    if request.method == "POST":
        form = PerfilForm(request.POST)
        print("empieza if 2")
        if form.is_valid():
            perfil = Perfil.objects.filter(usuario=usuario).update(**form.cleaned_data)
            return HttpResponseRedirect('/profile/')
            print("termina if 2 y da return http")
    
    else:

        perfil = Perfil.objects.filter(usuario=usuario)
        print("empieza if de else")
        if perfil.exists():
            perfil = perfil.first()
            form = PerfilForm(instance=perfil)
    context = {
        'form':form,
        'title':'Actualizar Perfil'
        }
    return render(request, 'register_profile.html', context)
        


@login_required(login_url='/login/')        
def register_inmueble(request):
    #POST
    usuario = request.user #nos traemos un objeto del tipo User, que viene del auth de django
    tipo_de_usuario = Perfil.objects.get(usuario=usuario).tipo_de_usuario.tipo_de_usuario
    if request.method == "POST":
        form = InmuebleForm(request.POST)
        if form.is_valid():
            usuario = usuario
            tipo_inmueble = form.cleaned_data['id_tipo_de_inmueble']
            comuna = form.cleaned_data['id_comuna']
            region = form.cleaned_data['id_region']
            nombre_inmueble = form.cleaned_data['nombre_inmueble']
            m2_construidos = form.cleaned_data['m2_construidos']
            numero_baños = form.cleaned_data['cantidad_baños']
            numero_habitaciones = form.cleaned_data['cantidad_habitaciones']
            direccion = form.cleaned_data['direccion']
            descripcion = form.cleaned_data['descripcion']
            
            datos = Inmueble(
                id_usuario=usuario,
                id_tipo_de_inmueble=tipo_inmueble,
                id_comuna=comuna,
                id_region=region,
                nombre_inmueble=nombre_inmueble,
                m2_construidos=m2_construidos, 
                cantidad_baños=numero_baños,
                cantidad_habitaciones=numero_habitaciones,
                direccion=direccion,
                descripcion=descripcion
            )
            datos.save()
            return HttpResponseRedirect('/inmuebles/')
    #vista GET
    else:
        form = InmuebleForm()
    context = {
        'form':form,
        'tipo':tipo_de_usuario,
        'title':'Registrar un Inmueble'
        }
    return render(request, 'register_inmueble.html', context)

def get_inmuebles(request):
    usuario = request.user
    tipo_de_usuario = Perfil.objects.get(usuario=usuario).tipo_de_usuario.tipo_de_usuario
    #otra forma es con el usuario = User.objects.get(username=username)
    inmuebles = Inmueble.objects.filter(id_usuario=usuario)
    context = {
        'inmuebles':inmuebles,
        'tipo':tipo_de_usuario,
        'title':'Registrar un Inmueble'
        }
    return render(request, 'inmuebles.html', context)


@login_required(login_url='/login/')
def update_inmueble(request, pk):
    usuario = request.user
    tipo = Perfil.objects.get(usuario=usuario).tipo_de_usuario.tipo_de_usuario
    inmueble = Inmueble.objects.get(pk=pk)

    if request.method =="POST":
        form = InmuebleForm(request.POST)
        if form.is_valid():
            inmueble = Inmueble.objects.filter(pk=pk).update(**form.cleaned_data)
            #el metodo update funciona solo con querysets por lo que no funcionara con el metodo get del object
            
            return HttpResponseRedirect('/inmuebles/')

    ###CON EL GET
    elif inmueble.id_usuario.id == usuario.id:
    #nos traemos el objeto Inmueble con pk = pk
        form = InmuebleForm(instance=inmueble)
        context = {
                    'form':form,
                    'title':'Editar Inmueble',
                    'tipo':tipo
                    }
    else:
        form = 'Inmueble no encontrado'
        context = {
                    'form':form,
                    'title':'Usted no tiene acceso a esta propiedad',
                    'tipo':tipo

                    }
    return render(request,'register_inmueble.html', context)


def contact(request, id):
    usuario = request.user
    tipo = Perfil.objects.get(usuario=usuario).tipo_de_usuario.tipo_de_usuario
    inmueble = Inmueble.objects.get(pk=id)
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            correo = form.cleaned_data['correo']
            nombre = form.cleaned_data['nombre']
            mensaje = form.cleaned_data['mensaje']
            nombre_inmueble = inmueble.nombre_inmueble
            arrendador = inmueble.id_usuario

            data = Contact(
                nombre_inmueble=nombre_inmueble,
                correo=correo,
                arrendador=arrendador,
                nombre=nombre,
                mensaje=mensaje,
            )
            data.save()
            return HttpResponseRedirect('/profile/')

    form = ContactForm()
    context = {
                'form':form,
                'title':'Contacta al Propietario',
                'tipo':tipo
            }
    return render(request,'register_inmueble.html', context)
    
def messages(request):
    usuario = request.user
    messages = Contact.objects.filter(arrendador=usuario)
    tipo = Perfil.objects.get(usuario=usuario).tipo_de_usuario.tipo_de_usuario

    context = {
                    'messages':messages,
                    'tipo':tipo
                }
    return render(request, 'contact.html', context)