from django.urls import path
from app.api.CostoProduccion.views import CostoPrduccionAV, CostoProduccionDetalleAV
from app.api.Intermediario.views import IntermediarioAV, IntermediarioDetalleAV
from app.api.Intermediario_Produccion.views import  IntermediarioProduccionDetalleAV, IntermediarioProduccionAV
from app.api.Parroquia.views import ParroquiaAV, ParroquiaDetalleAV
from app.api.Produccion.view import ProduccionAV, ProduccionDetalleAV
from app.api.Productor.views import ProductorAV, ProductorDetalleAV
from app.api.Canton.views import CantonDetalleAV,CantonAV
from app.api.Query.views import queryTotal
from app.api.Resultado.views import ResultadoAV, ResultadoDetalleAV
from app.api.TipoProductor.views import TipoProductoresAV
#from app.views import ListarCantones
#agregar una coleccionde urls
urlpatterns = [
   path('query-total/',queryTotal,name='query-listado'), 

   path('resultados/',ResultadoAV.as_view(),name='listar-resultados'), 
   path('resultados/<int:pk>',ResultadoDetalleAV.as_view(),name='detalle-resultados'),

   path('costo-produccion/',CostoPrduccionAV.as_view(),name='listar-costo-produccion'), 
   path('costo-produccion/<int:pk>',CostoProduccionDetalleAV.as_view(),name='detalle-costo-produccion'),

   path('cantones/',CantonAV.as_view(),name='listar-cantones'), 
   path('cantones/<int:pk>',CantonDetalleAV.as_view(),name='detalle-cantones'),

   path('parroquias/',ParroquiaAV.as_view(),name='listar-parroquias'),
   path('parroquias/<int:pk>',ParroquiaDetalleAV.as_view(),name='detalle-parroquias'),  

   path('productores/',ProductorAV.as_view(),name='listar-productores'),
   path('productores/<int:pk>',ProductorDetalleAV.as_view(),name='detalle-productores'),

   path('producciones/',ProduccionAV.as_view(),name='listar-producciones'),    
   path('producciones/<int:pk>',ProduccionDetalleAV.as_view(),name='detalle-producciones'),
      
   path('intermediarios/',IntermediarioAV.as_view(),name='listar-intermediarios'),    
   path('intermediarios/<int:pk>',IntermediarioDetalleAV.as_view(),name='detalle-intermediarios'),

   path('intermediarios-producciones/',IntermediarioProduccionAV.as_view(),name='listar-intermediarios-produccion'),    
   path('intermediarios-producciones/<int:pk>',IntermediarioProduccionDetalleAV.as_view(),name='detalle-intermediarios-produccion'),

   path('tipos-productores/',TipoProductoresAV.as_view(),name='tipos-productores'),   
]
