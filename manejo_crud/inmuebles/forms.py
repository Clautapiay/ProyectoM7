from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Perfil


class UserForm(UserCreationForm):
    

    class Meta():
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
        

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