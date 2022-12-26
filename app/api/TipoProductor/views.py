from urllib import response
from app.api.Canton.serializers import CantonSerializer
from app.api.TipoProductor.serializers import TipoProductorSerializer
from app.models import Canton, Tipo_Productor
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
#from rest_framework.permissions import IsAuthenticated
from app.api.permissions import AdminOrReadOnly

class TipoProductoresAV(APIView):
    ## SOLO PUEDE VISUALIZAR CUALQUIER PERSONA
    permission_classes =[AdminOrReadOnly]
    def get(self, request):
        try:
            tipoProductores = Tipo_Productor.objects.all()
            serializer = TipoProductorSerializer(tipoProductores, many=True)
            return Response({'data':serializer.data,'success':True,'message':'Listado de todos tipos de productores'},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'data':[],'success':False,'message':str(e)},status=status.HTTP_404_NOT_FOUND)
