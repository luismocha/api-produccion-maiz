from urllib import response
from app.api.Productor.serializer import ProductorSerializer
from app.models import Canton, Productor
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from app.api.permissions import AdminOrReadOnly
from rest_framework import serializers
from app.api.validaciones.validar_cedula import vcedula

class ProductorAV(APIView):
    permission_classes =[AdminOrReadOnly]
    def get(self, request):
        try:
            productor = Productor.objects.all()
            serializer = ProductorSerializer(productor, many=True)
            return Response({'data':serializer.data,'success':True,'message':'Listado de todos los productores'},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'data':[],'success':False,'message':"ERROR "+str(e)},status=status.HTTP_404_NOT_FOUND)
    def post(self, request):
        print("RESQUES")
        print(request.data)
        try:
            #validar productores con diferente cedula
            productor=Productor.objects.filter(cedula=request.data['cedula']).first()
            if  productor:
                return Response({'data':[],'success':False,'message':'Ya existe un productor con el mismo número de cédula'},status=status.HTTP_404_NOT_FOUND)
            ##VALIDAR CEDULA
            if not vcedula(request.data['cedula']):
                return Response({'data':[],'success':False,'message':'Número de cédula no valido'},status=status.HTTP_404_NOT_FOUND)
            ## TODO OK
            serializer=ProductorSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'data':serializer.data,'success':True,'message':'Productor creado exitosamente'},status=status.HTTP_201_CREATED)
            else:
                return Response({'data':serializer.errors,'success':False,'message':"No se puede crear el proveedor "}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'data':[],'success':False,'message':"ERROR "+str(e)},status=status.HTTP_404_NOT_FOUND)

#buscar por id
class ProductorDetalleAV(APIView):
    permission_classes =[AdminOrReadOnly]
    def get(self, request, pk):
        try:
            productor = Productor.objects.get(pk=pk)
            serializer = ProductorSerializer(productor)
            return Response({'data':serializer.data,'success':True,'message':'Productor encontrado'},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'data':[],'success':False,'message':'ERROR '+str(e)},status=status.HTTP_404_NOT_FOUND)
    #actulizar
    def put(self, request, pk):
        try:
            productor = Productor.objects.get(pk=pk)
        except Productor.DoesNotExist:
            return Response({'data':[],'success':False,'message':'Productor no encontrado'},status=status.HTTP_404_NOT_FOUND)
        ##VALIDAR CEDULA
        if not vcedula(request.data['cedula']):
            return Response({'data':[],'success':False,'message':'Número de cédula no valido'},status=status.HTTP_404_NOT_FOUND)
        ## TODO OK

        try:
            serializer=ProductorSerializer(productor,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'data':serializer.data,'success':True,'message':'Productor actualizado exitosamente'},status=status.HTTP_200_OK)
            else:
                return Response({'data':serializer.errors,'success':False,'message':'No se puede actulizar el productor'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'data':serializer.errors,'success':False,'message':"ERROR "+str(e)}, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk):
        try:
            productor = Productor.objects.get(pk=pk)
        except  Exception as e:
            return Response({'data':[],'success':False,'message':"ERROR "+str(e)},status=status.HTTP_404_NOT_FOUND)
        productor.delete()
        return Response({'data':[],'success':True,'message':'Registro eliminado'},status=status.HTTP_204_NO_CONTENT)

