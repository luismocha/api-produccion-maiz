from django.urls import path

from app.api.views import listarCantones
#from app.views import ListarCantones
#agregar una coleccionde urls
urlpatterns = [
   path('cantones/',listarCantones,name='listar-cantones') 
]
