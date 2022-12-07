from django.urls import path
from app.api.Parroquia.views import ParroquiaAV, ParroquiaDetalleAV

from app.api.views import CantonDetalleAV,CantonAV
#from app.views import ListarCantones
#agregar una coleccionde urls
urlpatterns = [
   path('cantones/',CantonAV.as_view(),name='listar-cantones'), 
   path('cantones/<int:pk>',CantonDetalleAV.as_view(),name='detalle-cantones'),
   path('parroquias/',ParroquiaAV.as_view(),name='listar-parroquias'),
   path('parroquias/<int:pk>',ParroquiaDetalleAV.as_view(),name='detalle-parroquias'),  
]