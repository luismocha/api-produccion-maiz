from rest_framework.response import Response
from django.db.models import Avg
from rest_framework.decorators import api_view
from rest_framework import status
#from app.api.Estadistico.serializers import EstadisticosSerializer
from app.models import Produccion,Productor
## obtener toda los resultados de las tablas
@api_view(['GET'])
def estadisticoProductores(request):
    #import pdb; pdb.set_trace()
    try:
        productores=Productor.objects.all()
        """ for productor in productores:
            for canton in productor.fK_canton.all():
                print(canton) """
        return Response({'data':[],'success':True,'message':'Ok'},status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'data':[],'success':False,'message':"ERROR "+str(e)}, status=status.HTTP_400_BAD_REQUEST)