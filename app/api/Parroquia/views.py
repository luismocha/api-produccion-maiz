from urllib import response
from app.api.Parroquia.serializers import ParroquiaSerializer
from app.models import Canton, Parroquia
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

class ParroquiaAV(APIView):
    def get(self, request):
        parroquias = Parroquia.objects.all()
        serializer = ParroquiaSerializer(parroquias, many=True)
        return Response(serializer.data)
    def post(self, request):
        print("RESQUES")
        print(request.data)
        try:
            serializer=ParroquiaSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(str(e))

#buscar por id
class ParroquiaDetalleAV(APIView):
    def get(self, request, pk):
        try:
            parroquia = Parroquia.objects.get(pk=pk)
            serializer = ParroquiaSerializer(parroquia)
            return Response(serializer.data,status=status.HTTP_200_OK)
        except:
            return Response({'error':'Parroquia no encontrada'},status=status.HTTP_404_NOT_FOUND)
    #actulizar
    def put(self, request, pk):
        try:
            parroquia = Parroquia.objects.get(pk=pk)
        except Canton.DoesNotExist:
            return Response({'error':'Parroquia no encontrado'},status=status.HTTP_404_NOT_FOUND)
        serializer=ParroquiaSerializer(parroquia,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk):
        try:
            parroquia = Parroquia.objects.get(pk=pk)
        except:
            return Response({'error':'Parroquia no encontrado'},status=status.HTTP_404_NOT_FOUND)
        parroquia.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

""" @api_view()
def listarCantones(request):
    cantones=Canton.objects.all()
    serializer=CantonSerializer(cantones,many=True)
    return response(serializer.data) """
""" class ListarCantones:
    pass """

