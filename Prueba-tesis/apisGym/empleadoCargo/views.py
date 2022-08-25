
from email import message
from unicodedata import name
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
from django.views import View
import json


from .models import Empleado

# Create your views here
# 
# 
# Una vista sirve para realizar una solicitud web y devuelve una respuesta WEB
# Esta clase para convertirlo en una vista que sea capaz de procesar las respuestas
# se tiene que importar en el archivo URL.py.

class EmpleadoVista(View):


    #metodo que se ejecuta cada vez que hago una petision, me muestra un mensaje si se realizo o no
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)



#----------------------------------------------------------------------

    def get(self, request, dni=0):

        #mcodigo para mostrar unico empleado
        if(dni>0):
            emple=list(Empleado.objects.filter(dni=dni).values())
            if len(emple) > 0:
                empleadoResultado = emple[0]
                datos = {'message': "Success", 'empleados': empleadoResultado}
            else:
                datos = {'message': "No existe empleado con ese DNI....................."}
            return JsonResponse(datos)
        

        #codigo para mostrar todos los empleados
        else:

            emple = list(Empleado.objects.values())
        
            if len(emple) > 0:
                datos = {'message': "Success", 'empleados': emple}
            else:
                datos = {'message': "error de datos....................."}
            return JsonResponse(datos) 
 



#-----------------------------------------------------------------

#INSERTAR EMPLEADO

#request es la peticion y el body es todo el cuerpo de esa peticion
    def post(self, request):

        jd =json.loads(request.body)   #js es abreviatura de jeson-data / lo otro significa cargar un jeson a partir de una respuesta de un body
        
        #proceso de insercion
        Empleado.objects.create(nombre=jd['nombre'],   apellido=jd['apellido'],   dni=jd['dni'] )


        datos = {'message':"Correcto"}
        return JsonResponse(datos)



#-----------------------------------------------------------------

#ACTUALIZAR UN EMPLEADO POR DNI

    def put(self, request, dni=0):
        jd =json.loads(request.body) 

        emple=list(Empleado.objects.filter(dni=dni).values())
        if len(emple) > 0:
            empleado = Empleado.objects.get(dni=dni)
            empleado.name=jd["nombre"]
            empleado.apellido=jd["apellido"]
            empleado.dni=jd["dni"]
            empleado.save()
            datos = {'message': "Empleado actualizao!!!!!"}
        else:
            datos = {'message': "Empleado no actualizado....................."}
        return JsonResponse(datos)

#-----------------------------------------------------------------

#Eliminar UN EMPLEADO POR DNI 

    def delete(self, request, dni):
        emple=list(Empleado.objects.filter(dni=dni).values())
        if len(emple) > 0:
            Empleado.objects.filter(dni=dni).delete()
            datos = {'message': "Eliminado correctamente"}
        else:
            datos = {'message': "No se puedo elimanar"}
        return JsonResponse(datos)

