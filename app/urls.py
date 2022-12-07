from django.urls import path

from app.api.views import CantonDetalleAV,CantonAV
#from app.views import ListarCantones
#agregar una coleccionde urls
urlpatterns = [
   path('cantones/',CantonAV.as_view(),name='listar-cantones'), 
   path('cantones/<int:pk>',CantonDetalleAV.as_view(),name='detalle-cantones') 
]
