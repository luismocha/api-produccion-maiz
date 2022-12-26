from urllib import response
from app.api.Canton.serializers import CantonSerializer
from app.models import Canton
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
#from rest_framework.permissions import IsAuthenticated
from app.api.permissions import AdminOrReadOnly

class CantonAV(APIView):
    ## SOLO PUEDE VISUALIZAR CUALQUIER PERSONA
    permission_classes =[AdminOrReadOnly]

    def get(self, request):
        try:
            cantons = Canton.objects.filter(activo=True)
            serializer = CantonSerializer(cantons, many=True)
            return Response({'data':serializer.data,'success':True,'message':'Listado de todos los cantones'},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'data':[],'success':False,'message':str(e)},status=status.HTTP_404_NOT_FOUND)
    
    def post(self, request):
        
        try:
            canton=Canton.objects.filter(nombre=request.data['nombre']).first()
            if  canton:
                return Response({'data':[],'success':False,'message':'Ya existe un cantón con el nombre de '+request.data['nombre']},status=status.HTTP_404_NOT_FOUND)
            ## TODO OK
            serializer=CantonSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'data':serializer.data,'success':True,'message':'Canton creado exitosamente'},status=status.HTTP_201_CREATED)
            else:
                return Response({'data':serializer.errors,'success':False,'message':'No se puede crear el cantón'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'data':serializer.errors,'success':False,'message':str(e)}, status=status.HTTP_400_BAD_REQUEST)

#buscar por id
class CantonDetalleAV(APIView):
    ## SOLO PUEDEN MANIPULAR LA INFORMACION LOS USUARIOS ADMIN
    permission_classes =[AdminOrReadOnly]
    def get(self, request, pk):
        try:
            canton = Canton.objects.get(pk=pk)
            serializer = CantonSerializer(canton)
            return Response({'data':serializer.data,'success':True,'message':'Cantón encontrado'},status=status.HTTP_200_OK)
        except:
            return Response({'data':[],'success':False,'message':'Cantón no encontrado'},status=status.HTTP_404_NOT_FOUND)
    #actulizar
    def put(self, request, pk):
        try:
            canton = Canton.objects.get(pk=pk)
        except Canton.DoesNotExist:
            return Response({'data':[],'success':False,'message':'Cantón no encontrado'},status=status.HTTP_404_NOT_FOUND)
        ## TODO OK
        try:
            serializer=CantonSerializer(canton,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'data':serializer.data,'success':True,'message':'Cantón actualizado exitosamente'},status=status.HTTP_200_OK)
            else:
                return Response({'data':serializer.errors,'success':False,'message':'No se puede actulizar el cantón'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'data':serializer.errors,'success':False,'message':"ERROR "+str(e)}, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk):
        try:
            canton = Canton.objects.get(pk=pk)
        except Exception as e:
            return Response({'data':[],'success':False,'message':str(e)},status=status.HTTP_404_NOT_FOUND)
        canton.delete()
        return Response({'data':[],'success':True,'message':'Registro eliminado'},status=status.HTTP_204_NO_CONTENT)

""" @api_view()
def listarCantones(request):
    cantones=Canton.objects.all()
    serializer=CantonSerializer(cantones,many=True)
    return response(serializer.data) """
""" class ListarCantones:
    pass """

