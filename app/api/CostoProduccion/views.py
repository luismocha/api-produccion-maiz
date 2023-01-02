from urllib import response
from app.api.CostoProduccion.serializers import CostoProduccionSerializer
from app.models import Costo_Produccion
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
#from rest_framework.permissions import IsAuthenticated
from app.api.permissions import AdminOrReadOnly

class CostoPrduccionAV(APIView):
    ## SOLO PUEDE VISUALIZAR CUALQUIER PERSONA
    permission_classes =[AdminOrReadOnly]

    def get(self, request):
        try:
            costo_produccion = Costo_Produccion.objects.filter(activo=True)
            serializer = CostoProduccionSerializer(costo_produccion, many=True)
            return Response({'data':serializer.data,'success':True,'message':'Listado de todos los costos de producción'},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'data':[],'success':False,'message':str(e)},status=status.HTTP_404_NOT_FOUND)
    
    def post(self, request):
        
        try:
            costo_produccion=Costo_Produccion.objects.filter(year=request.data['year']).first()
            if  costo_produccion:
                return Response({'data':[],'success':False,'message':'Ya existe un costo de produccion con el año '+str(request.data['year'])},status=status.HTTP_404_NOT_FOUND)
            ## TODO OK
            serializer=CostoProduccionSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'data':serializer.data,'success':True,'message':'Costo de producción creado exitosamente'},status=status.HTTP_201_CREATED)
            else:
                return Response({'data':serializer.errors,'success':False,'message':'No se puede crear el costo de producción'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'data':serializer.errors,'success':False,'message':"ERROR "+str(e)}, status=status.HTTP_400_BAD_REQUEST)

#buscar por id
class CostoProduccionDetalleAV(APIView):
    ## SOLO PUEDEN MANIPULAR LA INFORMACION LOS USUARIOS ADMIN
    permission_classes =[AdminOrReadOnly]
    def get(self, request, pk):
        try:
            costo_produccion = Costo_Produccion.objects.get(pk=pk)
            serializer = CostoProduccionSerializer(costo_produccion)
            return Response({'data':serializer.data,'success':True,'message':'Costro de producción encontrado'},status=status.HTTP_200_OK)
        except:
            return Response({'data':[],'success':False,'message':'Costo producción no encontrado'},status=status.HTTP_404_NOT_FOUND)
    #actulizar
    def put(self, request, pk):
        try:
            costo_produccion = Costo_Produccion.objects.get(pk=pk)
        except costo_produccion.DoesNotExist:
            return Response({'data':[],'success':False,'message':'Costo producción no encontrado'},status=status.HTTP_404_NOT_FOUND)
        ## TODO OK
        try:
            serializer=CostoProduccionSerializer(costo_produccion,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'data':serializer.data,'success':True,'message':'Costo producción actualizado exitosamente'},status=status.HTTP_200_OK)
            else:
                return Response({'data':serializer.errors,'success':False,'message':'No se puede actulizar el Costo de producción'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'data':serializer.errors,'success':False,'message':"ERROR "+str(e)}, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk):
        try:
            costo_produccion = Costo_Produccion.objects.get(pk=pk)
            #canton.delete()
            return Response({'data':[],'success':True,'message':'Solicitud exitosa, pero no se puede eliminar el registro por cuestion de reglas de negocio'},status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({'data':[],'success':False,'message':str(e)},status=status.HTTP_404_NOT_FOUND)

""" @api_view()
def listarCantones(request):
    cantones=Canton.objects.all()
    serializer=CantonSerializer(cantones,many=True)
    return response(serializer.data) """
""" class ListarCantones:
    pass """

