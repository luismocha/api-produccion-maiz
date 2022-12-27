from django.urls import path
from app.api.Parroquia.views import ParroquiaAV, ParroquiaDetalleAV
from app.api.Produccion.view import ProduccionAV, ProduccionDetalleAV
from app.api.Productor.views import ProductorAV, ProductorDetalleAV
from app.api.Canton.views import CantonDetalleAV,CantonAV
from app.api.TipoProductor.views import TipoProductoresAV
#from app.views import ListarCantones
#agregar una coleccionde urls
urlpatterns = [
   path('cantones/',CantonAV.as_view(),name='listar-cantones'), 
   path('cantones/<int:pk>',CantonDetalleAV.as_view(),name='detalle-cantones'),

   path('parroquias/',ParroquiaAV.as_view(),name='listar-parroquias'),
   path('parroquias/<int:pk>',ParroquiaDetalleAV.as_view(),name='detalle-parroquias'),  

   path('productores/',ProductorAV.as_view(),name='listar-productores'),
   path('productores/<int:pk>',ProductorDetalleAV.as_view(),name='detalle-productores'),

   path('producciones/',ProduccionAV.as_view(),name='listar-producciones'),    
   path('producciones/<int:pk>',ProduccionDetalleAV.as_view(),name='detalle-producciones'),

   path('tipos-productores/',TipoProductoresAV.as_view(),name='tipos-productores'),   
]
