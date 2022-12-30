from urllib import response
from app.api.Intermediario.serializers import IntermediarioSerializer
from app.api.Intermediario_Produccion.serializers import IntermediarioProduccionSerializer
from app.models import  Intermediario, Intermediario_Produccion
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from app.api.permissions import AdminOrReadOnly

class IntermediarioProduccionrioAV(APIView):
    permission_classes =[AdminOrReadOnly]
    def get(self, request):
        try:
            intermediarios_producciones = Intermediario_Produccion.objects.filter(activo=True)
            serializer = IntermediarioProduccionSerializer(intermediarios_producciones, many=True)
            return Response({'data':serializer.data,'success':True,'message':'Listado de todas los intermediarios con producciones'},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'data':[],'success':False,'message':"ERROR "+str(e)},status=status.HTTP_404_NOT_FOUND)
    def post(self, request):
        try:
            serializer=IntermediarioSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'data':serializer.data,'success':True,'message':'Intermediario creado exitosamente'},status=status.HTTP_201_CREATED)
            else:
                return Response({'data':serializer.errors,'success':False,'message':'No se puede crear el intermediario'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'data':serializer.errors,'success':False,'message':str(e)}, status=status.HTTP_400_BAD_REQUEST)

#buscar por id
class IntermediarioProduccionDetalleAV(APIView):
    permission_classes =[AdminOrReadOnly]
    def get(self, request, pk):
        try:
            intermediario = Intermediario.objects.get(pk=pk)
            serializer = IntermediarioSerializer(intermediario)
            return Response({'data':serializer.data,'success':True,'message':'Intermediario encontrada'},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'data':[],'success':False,'message':'ERROR '+str(e)},status=status.HTTP_404_NOT_FOUND)
    #actulizar
    def put(self, request, pk):
        try:
            intermediario = Intermediario.objects.get(pk=pk)
        except intermediario.DoesNotExist:
            return Response({'data':[],'success':False,'message':'Intermediario no encontrado'},status=status.HTTP_404_NOT_FOUND)

        ### TODO OK
        try:
            serializer=IntermediarioSerializer(intermediario,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'data':serializer.data,'success':True,'message':'Intermediario actualizado exitosamente'},status=status.HTTP_200_OK)
            else:
                return Response({'data':serializer.errors,'success':False,'message':'No se puede actulizar el intermediaro'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'data':serializer.errors,'success':False,'message':"ERROR "+str(e)}, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk):
        try:
            intermediario = Intermediario.objects.get(pk=pk)
        except Exception as e:
            return Response({'data':[],'success':False,'message':"ERROR"+str(e)},status=status.HTTP_404_NOT_FOUND)
        intermediario.delete()
        return Response({'data':[],'success':True,'message':'Registro eliminado'},status=status.HTTP_204_NO_CONTENT)



