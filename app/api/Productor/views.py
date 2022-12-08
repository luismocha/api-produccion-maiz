from urllib import response
from app.api.Productor.serializer import ProductorSerializer
from app.models import Canton, Productor
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

class ProductorAV(APIView):
    def get(self, request):
        productor = Productor.objects.all()
        serializer = ProductorSerializer(productor, many=True)
        return Response(serializer.data)
    def post(self, request):
        print("RESQUES")
        print(request.data)
        try:
            serializer=ProductorSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(str(e))

#buscar por id
class ProductorDetalleAV(APIView):
    def get(self, request, pk):
        try:
            productor = Productor.objects.get(pk=pk)
            serializer = ProductorSerializer(productor)
            return Response(serializer.data,status=status.HTTP_200_OK)
        except:
            return Response({'error':'Productor no encontrada'},status=status.HTTP_404_NOT_FOUND)
    #actulizar
    def put(self, request, pk):
        try:
            productor = Productor.objects.get(pk=pk)
        except Canton.DoesNotExist:
            return Response({'error':'Productor no encontrado'},status=status.HTTP_404_NOT_FOUND)
        serializer=ProductorSerializer(productor,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk):
        try:
            productor = Productor.objects.get(pk=pk)
        except:
            return Response({'error':'Productor no encontrado'},status=status.HTTP_404_NOT_FOUND)
        productor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

""" @api_view()
def listarCantones(request):
    cantones=Canton.objects.all()
    serializer=CantonSerializer(cantones,many=True)
    return response(serializer.data) """
""" class ListarCantones:
    pass """

