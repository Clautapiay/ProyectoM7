from .models import Usuario, Inmueble, Comuna, Region, Tipo_de_inmueble, Tipo_de_usuario, Perfil

#Para usuario arrendador
def publicar_propiedades(id_usuario, nombre_inmueble, m2_construidos, cantidad_estacionamientos, cantidad_habitaciones, cantidad_baños, direccion, id_region, id_comuna): #insertar inmueble
    datos_inmueble = Inmueble.objects.create(
            id_usuario=id_usuario,
            nombre_inmueble=nombre_inmueble,
            m2_construidos=m2_construidos,
            cantidad_estacionamientos=cantidad_estacionamientos,
            cantidad_habitaciones=cantidad_habitaciones,
            cantidad_baños=cantidad_baños,
            direccion=direccion,
            id_comuna=id_comuna,
            id_region=id_region,
        )
    datos_inmueble.save()
    return datos_inmueble
    
def listar_propiedades(): #obtener inmuebles
    lista_inmuebles = Tipo_de_inmueble.objects.all()
    return lista_inmuebles

def editar_propiedades(id_inmueble, nuevos_datos): #actualizar
    editar_inmueble = Inmueble.objects.get(id=id_inmueble)
    for key, value in nuevos_datos.items():
        setattr(editar_inmueble, key, value)
        editar_inmueble.save()
        return editar_inmueble

def eliminar_propiedades(id_inmueble): #borrar inmueble
    elim_inmueble = Inmueble.objects.get(id=id_inmueble)
    elim_inmueble.delete()
    return True

#def aceptar_arrendatarios():
    #pass
