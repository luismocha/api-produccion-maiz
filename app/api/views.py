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
        serializer=CantonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class 

""" @api_view()
def listarCantones(request):
    cantones=Canton.objects.all()
    serializer=CantonSerializer(cantones,many=True)
    return response(serializer.data) """
""" class ListarCantones:
    pass """

