from django.urls import path
from app.api.views import ListarCantones
#agregar una coleccionde urls
urlpatterns = [
   path('cantones/',ListarCantones,name='listar-cantones') 
]
