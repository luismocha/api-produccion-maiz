from urllib import response
from app.api.serializers import CantonSerializer
from app.models import Canton
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

class CantonAV(APIView):
    def get(self, request):
        cantons = Canton.objects.all()
        serializer = CantonSerializer(cantons, many=True)
        return Response(serializer.data)
    def post(self, request):
        try:
            serializer=CantonSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(str(e))

#buscar por id
class CantonDetalleAV(APIView):
    def get(self, request, pk):
        try:
            canton = Canton.objects.get(pk=pk)
            serializer = CantonSerializer(canton)
            return Response(serializer.data,status=status.HTTP_200_OK)
        except:
            return Response({'error':'Canton no encontrado'},status=status.HTTP_404_NOT_FOUND)
    #actulizar
    def put(self, request, pk):
        try:
            canton = Canton.objects.get(pk=pk)
        except Canton.DoesNotExist:
            return Response({'error':'Canton no encontrado'},status=status.HTTP_404_NOT_FOUND)
        serializer=CantonSerializer(canton,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk):
        try:
            canton = Canton.objects.get(pk=pk)
        except:
            return Response({'error':'Canton no encontrado'},status=status.HTTP_404_NOT_FOUND)
        canton.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

""" @api_view()
def listarCantones(request):
    cantones=Canton.objects.all()
    serializer=CantonSerializer(cantones,many=True)
    return response(serializer.data) """
""" class ListarCantones:
    pass """

