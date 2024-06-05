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



def get_list_inmuebles(comuna):
    select = f"""
    SELECT inmuebles_inmueble.id, nombre_inmueble, descripcion, comuna FROM inmuebles_inmueble
INNER JOIN inmuebles_region
	ON id_region_id = inmuebles_region.id
INNER JOIN inmuebles_comuna
	on id_comuna_id = inmuebles_comuna.id
--WHERE comuna like '{comuna}'
    """

    query = Inmueble.objects.raw(select)

    # archivo = open('nombre_descripcion.txt',"a") en este caso el archivo.close debe ir fuera del for
    for p in query:
        archivo = open(f'{p.comuna}.txt',"a")
        print(p.nombre_inmueble)
        print(p.id_comuna)
        print(p.id_region)
        print(p.direccion)
        print(p.descripcion)
        archivo.write(f"Nombre Comuna: {p.comuna}\n")
        archivo.write(f"Nombre del inmueble: {p.nombre_inmueble}\n")
        archivo.write(f"Descripcion: {p.descripcion}\n")
        archivo.close() #archivo.close debe ir dentro del for, para que asi cree un arch de cada comuna sin error


def get_list_region(region):
    select = f"""
    SELECT inmuebles_inmueble.id, nombre_inmueble, descripcion, region FROM inmuebles_inmueble
INNER JOIN inmuebles_region
	ON id_region_id = inmuebles_region.id
INNER JOIN inmuebles_comuna
	on id_comuna_id = inmuebles_comuna.id
--WHERE comuna like '{region}'
    """

    query = Inmueble.objects.raw(select)

    archivo = open('region.txt',"a")
    for p in query:
        print(p.nombre_inmueble)
        print(p.id_comuna)
        print(p.id_region)
        print(p.direccion)
        print(p.descripcion)
        archivo.write(f"Nombre Region: {p.region}\n")
        archivo.write(f"Nombre del inmueble: {p.nombre_inmueble}\n")
        archivo.write(f"Descripcion: {p.descripcion}\n")
    archivo.close()


