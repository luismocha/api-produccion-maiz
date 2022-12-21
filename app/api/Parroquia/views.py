from urllib import response
from app.api.Parroquia.serializers import ParroquiaSerializer
from app.models import Canton, Parroquia
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from app.api.permissions import AdminOrReadOnly
import json
class ParroquiaAV(APIView):
    permission_classes =[AdminOrReadOnly]
    def get(self, request):
        try:
            parroquias = Parroquia.objects.filter(activo=True)
            serializer = ParroquiaSerializer(parroquias, many=True)
            return Response({'data':serializer.data,'success':True,'message':'Listado de todas las parroquias'},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'data':[],'success':False,'message':str(e)},status=status.HTTP_404_NOT_FOUND)
    def post(self, request):
        try:
            serializer=ParroquiaSerializer(data=request.data)
            
            if serializer.is_valid():
                serializer.save()
                return Response({'data':serializer.data,'success':True,'message':'Parroquia creada exitosamente'},status=status.HTTP_201_CREATED)
            else:
                return Response({'data':serializer.errors,'success':False,'message':'No se puede crear la parroquia'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'data':serializer.errors,'success':False,'message':str(e)}, status=status.HTTP_400_BAD_REQUEST)

#buscar por id
class ParroquiaDetalleAV(APIView):
    permission_classes =[AdminOrReadOnly]
    def get(self, request, pk):
        try:
            parroquia = Parroquia.objects.get(pk=pk)
            serializer = ParroquiaSerializer(parroquia)
            return Response({'data':serializer.data,'success':True,'message':'Parroquia encontrada'},status=status.HTTP_200_OK)
        except:
            return Response({'data':[],'success':False,'message':'Parroquia no encontrada'},status=status.HTTP_404_NOT_FOUND)
    #actulizar
    def put(self, request, pk):
        try:
            parroquia = Parroquia.objects.get(pk=pk)
        except Parroquia.DoesNotExist:
            return Response({'data':[],'success':False,'message':'Parroquia no encontrada'},status=status.HTTP_404_NOT_FOUND)

        ### TODO OK
        try:
            serializer=ParroquiaSerializer(parroquia,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'data':serializer.data,'success':True,'message':'Parroquia actualizada exitosamente'},status=status.HTTP_200_OK)
            else:
                return Response({'data':serializer.errors,'success':False,'message':'No se puede actulizar la parroquia'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'data':serializer.errors,'success':False,'message':str(e)}, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk):
        try:
            parroquia = Parroquia.objects.get(pk=pk)
        except Exception as e:
            return Response({'data':[],'success':False,'message':str(e)},status=status.HTTP_404_NOT_FOUND)
        parroquia.delete()
        return Response({'data':[],'success':True,'message':'Registro eliminado'},status=status.HTTP_204_NO_CONTENT)

""" @api_view()
def listarCantones(request):
    cantones=Canton.objects.all()
    serializer=CantonSerializer(cantones,many=True)
    return response(serializer.data) """
""" class ListarCantones:
    pass """

