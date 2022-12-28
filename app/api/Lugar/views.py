from urllib import response
from app.api.Lugar.serializers import LugarSerializer
from app.models import  Lugar
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
#from rest_framework.permissions import IsAuthenticated
from app.api.permissions import AdminOrReadOnly

class LugarAV(APIView):
    ## SOLO PUEDE VISUALIZAR CUALQUIER PERSONA
    permission_classes =[AdminOrReadOnly]
    def get(self, request):
        try:
            lugars = Lugar.objects.filter(activo=True)
            serializer = LugarSerializer(lugars, many=True)
            return Response({'data':serializer.data,'success':True,'message':'Listado de todos los lugares'},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'data':[],'success':False,'message':str(e)},status=status.HTTP_404_NOT_FOUND)
    
    def post(self, request):
        
        try:
            lugar=Lugar.objects.filter(nombre=request.data['nombre']).first()
            if  lugar:
                return Response({'data':[],'success':False,'message':'Ya existe un lugar con el nombre de '+request.data['nombre']},status=status.HTTP_404_NOT_FOUND)
            ## TODO OK
            serializer=LugarSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'data':serializer.data,'success':True,'message':'Lugar creado exitosamente'},status=status.HTTP_201_CREATED)
            else:
                return Response({'data':serializer.errors,'success':False,'message':'No se puede crear el lugar'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'data':serializer.errors,'success':False,'message':"ERROR "+str(e)}, status=status.HTTP_400_BAD_REQUEST)
 
#buscar por id
class LugarDetalleAV(APIView):
    permission_classes =[AdminOrReadOnly]
    def get(self, request, pk):
        try:
            lugars = Lugar.objects.get(pk=pk)
            serializer = LugarSerializer(lugars)
            return Response({'data':serializer.data,'success':True,'message':'Lugar encontrado'},status=status.HTTP_200_OK)
        except:
            return Response({'data':[],'success':False,'message':'Lugar no encontrado'},status=status.HTTP_404_NOT_FOUND)
    #actulizar
    def put(self, request, pk):
        try:
            lugar = Lugar.objects.get(pk=pk)
        except Lugar.DoesNotExist:
            return Response({'data':[],'success':False,'message':'Lugar no encontrado'},status=status.HTTP_404_NOT_FOUND)
        ## TODO OK ##
        try:
            serializer=LugarSerializer(lugar,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'data':serializer.data,'success':True,'message':'Lugar actualizado exitosamente'},status=status.HTTP_200_OK)
            else:
                return Response({'data':serializer.errors,'success':False,'message':'No se puede actulizar el lugar'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'data':serializer.errors,'success':False,'message':"ERROR "+str(e)}, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk):
        try:
            lugar = Lugar.objects.get(pk=pk)
        except Exception as e:
            return Response({'data':[],'success':False,'message':"ERROR "+str(e)},status=status.HTTP_404_NOT_FOUND)
        lugar.delete()
        return Response({'data':[],'success':True,'message':'Registro eliminado'},status=status.HTTP_204_NO_CONTENT) 

