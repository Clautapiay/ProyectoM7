from django.shortcuts import render, HttpResponse, HttpResponseRedirect, get_object_or_404
from .models import Inmueble, Perfil
from .forms import UserForm, PerfilForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.
# def index(request):
#     return HttpResponse('Hola Mundo')
@login_required(login_url='/login/')
def index(request):
    inmuebles = Inmueble.objects.all()
    context = {
        'inmuebles': inmuebles
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
    perfil = Perfil.objects.filter(usuario=usuario)
    if perfil.exists():
        perfil=perfil[0]
    else:
        perfil = None
    context = {'perfil':perfil}
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
        


        