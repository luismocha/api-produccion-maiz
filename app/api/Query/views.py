from rest_framework.response import Response
from django.db.models import Avg
from rest_framework.decorators import api_view,permission_classes
from app.api.Query.serializers import ResultadoTablasAppSerializer
from rest_framework import status
from app.api.permissions import AdminAuthPutOrReadOnly, AdminOrReadOnly, AuthPermisos
from app.models import Produccion
## obtener toda los resultados de las tablas
@api_view(['POST'])
@permission_classes([AdminAuthPutOrReadOnly])
def queryTotal(request):
    #import pdb; pdb.set_trace()
    try:
        
        serializer=ResultadoTablasAppSerializer(data=request.data)
        if serializer.is_valid():
            yearCadena=request.data['year']
            if not yearCadena.isnumeric():
                return Response({'data':[],'success':False,'message':'El año debe ser númerico'},status=status.HTTP_404_NOT_FOUND)
            #****** HACEMOS LAS CONSULTAS TODO OK ******
            #1. sumar todas las hectarias de la tabla produccion y sacar un promedio
            #import pdb; pdb.set_trace()
            ## validar si existe produccion de ese año
            existeProduccion=Produccion.objects.filter(year=yearCadena).first()
            if not existeProduccion:
                return Response({'data':[],'success':False,'message':'No existe producción disponible para el año '+yearCadena},status=status.HTTP_404_NOT_FOUND)
            totalHectarias=Produccion.objects.filter(year=yearCadena).aggregate(Avg('hectareas'))
            totalPrecioVenta=Produccion.objects.filter(year=yearCadena).aggregate(Avg('precio_venta'))
            #totalQuintales=Produccion.objects.filter(year=yearCadena).aggregate(Avg('quintales'))
            totalToneladas=Produccion.objects.filter(year=yearCadena).aggregate(Avg('toneladas'))
            numeroHectarias=Produccion.objects.filter(year=yearCadena).count()
            data={
                'costoTotalProduccion':{
                    'numeroHectarias':numeroHectarias,
                    'costoTotalProduccionPorHectaria':totalHectarias['hectareas__avg'],
                },
                'rentabilidad':{
                    'precioVentaAlMercado':totalPrecioVenta['precio_venta__avg']//totalToneladas['toneladas__avg'],
                    'rendimientoCultivo': totalToneladas['toneladas__avg']//totalHectarias['hectareas__avg']
                }
            }
            return Response({'data':data,'success':True,'message':'Ok'},status=status.HTTP_200_OK)
        return Response({'data':serializer.errors,'success':False,'message':'El formato del año no es el correcto'},status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'data':serializer.errors,'success':False,'message':"ERROR "+str(e)}, status=status.HTTP_400_BAD_REQUEST)