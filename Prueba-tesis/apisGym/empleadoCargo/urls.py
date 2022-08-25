from django.urls import path
from .views import EmpleadoVista
#path permite establecer una ruta

#Se crea una lista de rutas 


#path== la ruta raiz de nuestra aplicacion que nos va a devolver todos los empleados
#EmpleadoVista.as_view() == Es la vista creada e importada
#name == el nobre de la url (SE LE LLAMA TAMBIEN ENDPOINT)

urlpatterns = [
    path('',EmpleadoVista.as_view(), name='empleado_lista'),
    path('/<int:dni>',EmpleadoVista.as_view(), name='empleado_por_nombre') #url para buscar por dni
    
]