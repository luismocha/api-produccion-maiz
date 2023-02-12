from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from app.api.Publicaciones.serializers import PublicacionesSerializer
from app.api.permissions import AdminOrReadOnly
import uuid
from app.models import Publicaciones
class PublicacionesAV(APIView):
    permission_classes =[AdminOrReadOnly]
    def get(self, request):
        try:
            galeria = Publicaciones.objects.all()
            serializer = PublicacionesSerializer(galeria, many=True)
            return Response({'data':serializer.data,'success':True,'message':'Listado de todas las publicaciones'},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'data':[],'success':False,'message':"ERROR "+str(e)},status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        try:
            file=request.data['archivo']
            ext = file.name.split('.')[-1]
            nuevoNombreFile = "%s.%s" % (uuid.uuid4(), ext)
            file._name=nuevoNombreFile
            data={
                    'nombre':request.data['nombre'],
                    'archivo':request.data['archivo'],
                    'descripcion':request.data['descripcion']
            } 
            serializer=PublicacionesSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response({'data':serializer.data,'success':True,'message':'Publicación creada exitosamente'},status=status.HTTP_201_CREATED)
            else:
                return Response({'data':serializer.errors,'success':False,'message':'No se puede crear la publicación'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'data':serializer.errors,'success':False,'message':"ERROR "+str(e)}, status=status.HTTP_400_BAD_REQUEST)
#buscar por id
class PublicacionesDetalleAV(APIView):
    permission_classes =[AdminOrReadOnly]
    def get(self, request, pk):
        try:
            publicacion = Publicaciones.objects.get(pk=pk)
            serializer = PublicacionesSerializer(publicacion)
            return Response({'data':serializer.data,'success':True,'message':'Galeria no encontrada'},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'data':[],'success':False,'message':'ERROR '+str(e)},status=status.HTTP_404_NOT_FOUND)
    #actulizar
    def put(self, request, pk):
        try:
            publicacion = Publicaciones.objects.get(pk=pk)
        except Publicaciones.DoesNotExist:
            return Response({'data':[],'success':False,'message':'Publicación no encontrado'},status=status.HTTP_404_NOT_FOUND)

        ### TODO OK
        try:
            serializer=PublicacionesSerializer(publicacion,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'data':serializer.data,'success':True,'message':'Publicación actualizado exitosamente'},status=status.HTTP_200_OK)
            else:
                return Response({'data':serializer.errors,'success':False,'message':'No se puede actulizar la publicación'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'data':serializer.errors,'success':False,'message':"ERROR "+str(e)}, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk):
        try:
            publicacion = Publicaciones.objects.get(pk=pk)
            publicacion.delete()
            return Response({'data':[],'success':True,'message':'Registro eliminado'},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'data':[],'success':False,'message':str(e)},status=status.HTTP_404_NOT_FOUND)