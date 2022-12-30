from urllib import response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from app.api.Intermediario.serializers import IntermediarioSerializer
#from rest_framework.permissions import IsAuthenticated
from app.api.permissions import AdminOrReadOnly
from app.models import Intermediario

class IntermediarioAV(APIView):
    ## SOLO PUEDE VISUALIZAR CUALQUIER PERSONA
    permission_classes =[AdminOrReadOnly]
    def get(self, request):
        try:
            intermediarios = Intermediario.objects.filter(activo=True)
            serializer = IntermediarioSerializer(intermediarios, many=True)
            return Response({'data':serializer.data,'success':True,'message':'Listado de todos los intermediarios'},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'data':[],'success':False,'message':str(e)},status=status.HTTP_404_NOT_FOUND)
    
    def post(self, request):
        
        try:
            intermediario=Intermediario.objects.filter(lugar=request.data['lugar']).first()
            if  intermediario:
                return Response({'data':[],'success':False,'message':'Ya existe un intermediario con el nombre de '+request.data['lugar']},status=status.HTTP_404_NOT_FOUND)
            ## TODO OK
            serializer=IntermediarioSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'data':serializer.data,'success':True,'message':'Intermediario creado exitosamente'},status=status.HTTP_201_CREATED)
            else:
                return Response({'data':serializer.errors,'success':False,'message':'No se puede crear el intermediario'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'data':serializer.errors,'success':False,'message':"ERROR "+str(e)}, status=status.HTTP_400_BAD_REQUEST)
 
#buscar por id
class IntermediarioDetalleAV(APIView):
    permission_classes =[AdminOrReadOnly]
    def get(self, request, pk):
        try:
            lugars = Intermediario.objects.get(pk=pk)
            serializer = IntermediarioSerializer(lugars)
            return Response({'data':serializer.data,'success':True,'message':'Intermediario encontrado'},status=status.HTTP_200_OK)
        except:
            return Response({'data':[],'success':False,'message':'Intermediario no encontrado'},status=status.HTTP_404_NOT_FOUND)
    #actulizar
    def put(self, request, pk):
        try:
            lugar = Intermediario.objects.get(pk=pk)
        except lugar.DoesNotExist:
            return Response({'data':[],'success':False,'message':'Intermediario no encontrado'},status=status.HTTP_404_NOT_FOUND)
        ## TODO OK ##
        try:
            serializer=IntermediarioSerializer(lugar,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'data':serializer.data,'success':True,'message':'Intermediario actualizado exitosamente'},status=status.HTTP_200_OK)
            else:
                return Response({'data':serializer.errors,'success':False,'message':'No se puede actulizar el intermediario'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'data':serializer.errors,'success':False,'message':"ERROR "+str(e)}, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk):
        try:
            intermediario = Intermediario.objects.get(pk=pk)
        except Exception as e:
            return Response({'data':[],'success':False,'message':"ERROR "+str(e)},status=status.HTTP_404_NOT_FOUND)
        intermediario.delete()
        return Response({'data':[],'success':True,'message':'Registro eliminado'},status=status.HTTP_204_NO_CONTENT) 

