from .models import Inmueble

query =  "SELECT * FROM app_inmuebles"

inmuebles = Inmueble.objects.raw(query)


