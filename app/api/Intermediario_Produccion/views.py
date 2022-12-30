from urllib import response
from app.api.Intermediario.serializers import IntermediarioSerializer
from app.api.Intermediario_Produccion.serializers import IntermediarioProduccionSerializer
from app.models import  Intermediario, Intermediario_Produccion, Produccion
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from app.api.permissions import AdminOrReadOnly

class IntermediarioProduccionAV(APIView):
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
            #import pdb; pdb.set_trace()
            ### ******** validar que esta produccion exista ********** ##
            produccion=Produccion.objects.filter(pk=request.data['fk_produccion_id']).first()
            if not produccion:
                return Response({'data':[],'success':False,'message':"Produccion no encontrada "},status=status.HTTP_404_NOT_FOUND)
            
            ##******* validar que exista stock ************* ####
            existeStock=False
            if produccion.stock>=request.data['cantidad_comprada']:
                existeStock=True
            if not existeStock:
                return Response({'data':[],'success':False,'message':"No existe stock suficiente en la producción, el stock actual es de "+str(produccion.stock)},status=status.HTTP_404_NOT_FOUND)
            
            ## ********* EL AÑO DE COMPRA DEBE SER IGUAL AL AÑO DE PRODUCCION *********##
            yerCompraIsIgualproduccionYear =False
            if produccion.year== request.data['year_compra']:
                yerCompraIsIgualproduccionYear=True
            if not yerCompraIsIgualproduccionYear:
                return Response({'data':[],'success':False,'message':"El año de compra de la producción debe ser igual al de la producción, El año de la producción es: "+str(produccion.year)},status=status.HTTP_404_NOT_FOUND)
            
            ## ******** VALIDAR EL INTERMEDIARIO EXISTA ****************###3
            intermediario=Intermediario.objects.filter(pk=request.data['fk_intermediario_id']).first()
            if not intermediario:
                return Response({'data':[],'success':False,'message':"Intermediario no encontrado"},status=status.HTTP_404_NOT_FOUND)
            

            ## ******* TODO Ok*****************#####
            ## 1. REGISTRO LA PRODUCCION-INTERMEDARIO
            #import pdb; pdb.set_trace()
            serializerIntermediarioProduccion=IntermediarioProduccionSerializer(data=request.data)
            if not serializerIntermediarioProduccion.is_valid():
                return Response({'data':serializerIntermediarioProduccion.errors,'success':False,'message':'No se puede crear el intermediario'}, status=status.HTTP_400_BAD_REQUEST)
            ## GUARADAMOS EL REGISTRO   
            serializerIntermediarioProduccion.save()
            
            ##**********  ACTUALIZAR EL STOCK DE LA PRODUCCION **************###
            #import pdb; pdb.set_trace()
            produccion.stock=produccion.stock-request.data['cantidad_comprada']
            produccion.save()
            return Response({'data':serializerIntermediarioProduccion.data,'success':True,'message':'Intermediario Producción creado exitosamente'},status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'data':[],'success':False,'message':"ERROR "+str(e)}, status=status.HTTP_400_BAD_REQUEST)

#buscar por id
class IntermediarioProduccionDetalleAV(APIView):
    permission_classes =[AdminOrReadOnly]
    def get(self, request, pk):
        try:
            intermediarioProduccion = Intermediario_Produccion.objects.get(pk=pk)
            serializer = IntermediarioProduccionSerializer(intermediarioProduccion)
            return Response({'data':serializer.data,'success':True,'message':'Intermediario Producción encontrado'},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'data':[],'success':False,'message':'ERROR '+str(e)},status=status.HTTP_404_NOT_FOUND)
    #actulizar
    def put(self, request, pk):
        try:
            intermediarioProduccion = Intermediario_Produccion.objects.get(pk=pk)
        except intermediarioProduccion.DoesNotExist:
            return Response({'data':[],'success':False,'message':'Intermediario Producción no encontrado'},status=status.HTTP_404_NOT_FOUND)

        try:
            ### ******** validar que esta produccion exista ********** ##
            produccion=Produccion.objects.filter(pk=request.data['fk_produccion_id']).first()
            if not produccion:
                return Response({'data':[],'success':False,'message':"Produccion no encontrada "},status=status.HTTP_404_NOT_FOUND)
            
            ##******* validar que exista stock ************* ####
            existeStock=False
            if produccion.stock>=request.data['cantidad_comprada']:
                existeStock=True
            if not existeStock:
                return Response({'data':[],'success':False,'message':"No existe stock suficiente en la producción, el stock actual es de "+str(produccion.stock)},status=status.HTTP_404_NOT_FOUND)
            
            ## ********* EL AÑO DE COMPRA DEBE SER IGUAL AL AÑO DE PRODUCCION *********##
            yerCompraIsIgualproduccionYear =False
            if produccion.year== request.data['year_compra']:
                yerCompraIsIgualproduccionYear=True
            if not yerCompraIsIgualproduccionYear:
                return Response({'data':[],'success':False,'message':"El año de compra de la producción debe ser igual al de la producción, El año de la producción es: "+str(produccion.year)},status=status.HTTP_404_NOT_FOUND)
            
            ## ******** VALIDAR EL INTERMEDIARIO EXISTA ****************###3
            intermediario=Intermediario.objects.filter(pk=request.data['fk_intermediario_id']).first()
            if not intermediario:
                return Response({'data':[],'success':False,'message':"Intermediario no encontrado"},status=status.HTTP_404_NOT_FOUND)

            serializer=IntermediarioProduccionSerializer(intermediarioProduccion,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'data':serializer.data,'success':True,'message':'Intermediario Producción actualizado exitosamente'},status=status.HTTP_200_OK)
            else:
                return Response({'data':serializer.errors,'success':False,'message':'No se puede actulizar el Intermediario Producción'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'data':serializer.errors,'success':False,'message':"ERROR "+str(e)}, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk):
        try:
            intermediarioProduccion = Intermediario_Produccion.objects.get(pk=pk)
        except Exception as e:
            return Response({'data':[],'success':False,'message':"ERROR "+str(e)},status=status.HTTP_404_NOT_FOUND)
        intermediarioProduccion.delete()
        return Response({'data':[],'success':True,'message':'Registro eliminado'},status=status.HTTP_204_NO_CONTENT)



