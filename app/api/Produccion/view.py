from rest_framework.views import APIView
from rest_framework.response import Response
from app.api.Produccion.serializer import ProduccionSerializer
from app.api.permissions import AdminOrReadOnly
from app.models import Produccion
from rest_framework import status

class ProduccionAV(APIView):
    permission_classes =[AdminOrReadOnly]
    def get(self, request):
        #import pdb; pdb.set_trace()
        try:
            producciones = Produccion.objects.filter(activo=True)
            serializer = ProduccionSerializer(producciones, many=True)
            return Response({'data':serializer.data,'success':True,'message':'Listado de todas las producciones'},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'data':[],'success':False,'message':"ERROR "+str(e)},status=status.HTTP_404_NOT_FOUND)
    def post(self, request):
        #import pdb; pdb.set_trace()
        try:
            ##el usuario solo puede tener una produccion por año
            produccion=Produccion.objects.filter(fk_productor=request.data['fk_productor_id'],year=request.data['year'],activo=True).first()
            if  produccion:
                return Response({'data':[],'success':False,'message':'Ya existe una producción registrada con el mismo productor y el mismo año'},status=status.HTTP_404_NOT_FOUND)
            ###### TODO OK
            serializer=ProduccionSerializer( data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'data':serializer.data,'success':True,'message':'Producción creada exitosamente'},status=status.HTTP_201_CREATED)
            else:
                return Response({'data':serializer.errors,'success':False,'message':'No se puede crear la Producción'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'data':serializer.errors,'success':False,'message':"ERROR "+str(e)}, status=status.HTTP_400_BAD_REQUEST)