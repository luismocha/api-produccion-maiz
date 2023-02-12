from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from app.api.Galeria.serializers import GaleriaSerializer
from app.api.permissions import AdminOrReadOnly
from app.models import Galeria
import uuid
class GaleriaAV(APIView):
    permission_classes =[AdminOrReadOnly]
    def get(self, request):
        try:
            galeria = Galeria.objects.all()
            serializer = GaleriaSerializer(galeria, many=True)
            return Response({'data':serializer.data,'success':True,'message':'Listado de todas las galerias'},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'data':[],'success':False,'message':"ERROR "+str(e)},status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        try:
            file=request.data['imagen']
            ext = file.name.split('.')[-1]
            nuevoNombreFile = "%s.%s" % (uuid.uuid4(), ext)
            file._name=nuevoNombreFile
            data={
                    'nombre':request.data['nombre'],
                    'imagen':request.data['imagen'],
                    'descripcion':request.data['descripcion']
            } 
            serializer=GaleriaSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response({'data':serializer.data,'success':True,'message':'Resultado creada exitosamente'},status=status.HTTP_201_CREATED)
            else:
                return Response({'data':serializer.errors,'success':False,'message':'No se puede crear el resultado'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'data':serializer.errors,'success':False,'message':"ERROR "+str(e)}, status=status.HTTP_400_BAD_REQUEST)
#buscar por id
class GaleriaDetalleAV(APIView):
    permission_classes =[AdminOrReadOnly]
    def get(self, request, pk):
        try:
            resultado = Galeria.objects.get(pk=pk)
            serializer = GaleriaSerializer(resultado)
            return Response({'data':serializer.data,'success':True,'message':'Galeria no encontrada'},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'data':[],'success':False,'message':'ERROR '+str(e)},status=status.HTTP_404_NOT_FOUND)
    #actulizar
    def put(self, request, pk):
        try:
            galeria = Galeria.objects.get(pk=pk)
        except Galeria.DoesNotExist:
            return Response({'data':[],'success':False,'message':'Galeria no encontrado'},status=status.HTTP_404_NOT_FOUND)

        ### TODO OK
        try:
            serializer=GaleriaSerializer(galeria,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'data':serializer.data,'success':True,'message':'Galeria actualizado exitosamente'},status=status.HTTP_200_OK)
            else:
                return Response({'data':serializer.errors,'success':False,'message':'No se puede actulizar la galeria'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'data':serializer.errors,'success':False,'message':"ERROR "+str(e)}, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk):
        try:
            galeria = Galeria.objects.get(pk=pk)
            galeria.delete()
            return Response({'data':[],'success':True,'message':'Registro eliminado'},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'data':[],'success':False,'message':str(e)},status=status.HTTP_404_NOT_FOUND)