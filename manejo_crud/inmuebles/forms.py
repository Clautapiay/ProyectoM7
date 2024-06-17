from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Perfil, Inmueble, Contact


class UserForm(UserCreationForm):
    
    class Meta():
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
        labels = {
            'username':'Nombre de usuario',
            'first_name':'Nombre',
            'last_name':'Apellido',
            'email':'Correo Electronico',
            'password1':'Contraseña',
            'password2':'Repita la Contraseña' 
        }
        

# class PerfilForm(forms.Form):
#     TIPO =((1,'Arrendador'),(2,'Arrendatario')) #lo primero es el dato que se entrega y lo segundo lo que se muestra en el formulario
# #correo y usuario se puede obtener desde auth.user, porque se almacenan al iniciar sesión en el sistema
#     tipo = forms.ChoiceField(choices=[TIPO], required=True)
#     rut = forms.CharField(label='rut', max_length=50)
#     direccion = forms.CharField(label='direccion', max_length=100)
#     telefono_personal = forms.CharField(label='telefono', max_length=100)


class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ('tipo_de_usuario','rut','direccion','telefono_personal')

class InmuebleForm(forms.ModelForm):
    class Meta:

        model = Inmueble
        fields = ('id_tipo_de_inmueble', 'id_comuna', 'id_region',
                'nombre_inmueble', 'm2_construidos', 'cantidad_baños', 
                'cantidad_habitaciones', 'cantidad_estacionamientos',
                'direccion', 'descripcion', 'precio_mensual_arriendo')
        
        labels = {
                'id_tipo_de_inmueble':'Tipo de Inmueble', 
                'id_comuna':'Comuna',
                'id_region':'Región',
                'nombre_inmueble':'Nombre Inmueble',
                'm2_construidos':'Metros Cuadrados Construidos',
                'cantidad_baños':'Número de Baños', 
                'cantidad_habitaciones':'Número de Habitaciones',
                'cantidad_estacionamientos':'Número de estacionamientos',
                'direccion':'Dirección', 
                'descripcion':'Descripción',
                'precio_mensual_arriendo':'Precio mensual del Arriendo'}       
        #'__all__' registra todos los campos disponibles del modelo
        #m2_totales, id_usuario


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('correo','nombre','mensaje')