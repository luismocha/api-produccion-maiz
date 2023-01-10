from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from app.api.Resultado.serializers import ResultadoSerializer
from app.api.permissions import AdminOrReadOnly
from app.models import Resultado

class ResultadoAV(APIView):
    permission_classes =[AdminOrReadOnly]
    def get(self, request):
        try:
            resultado = Resultado.objects.all()
            serializer = ResultadoSerializer(resultado, many=True)
            return Response({'data':serializer.data,'success':True,'message':'Listado de todas los resultados'},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'data':[],'success':False,'message':"ERROR "+str(e)},status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        try:
            resultado=Resultado.objects.filter(year=request.data['year']).first()
            if  resultado:
                return Response({'data':[],'success':False,'message':'Ya existe un resultado con el mismo año '+request.data['year']},status=status.HTTP_404_NOT_FOUND)
            ###### TODO OK
            serializer=ResultadoSerializer(data=request.data)
            
            if serializer.is_valid():
                serializer.save()
                return Response({'data':serializer.data,'success':True,'message':'Resultado creada exitosamente'},status=status.HTTP_201_CREATED)
            else:
                return Response({'data':serializer.errors,'success':False,'message':'No se puede crear el resultado'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'data':serializer.errors,'success':False,'message':"ERROR "+str(e)}, status=status.HTTP_400_BAD_REQUEST)
#buscar por id
class ResultadoDetalleAV(APIView):
    permission_classes =[AdminOrReadOnly]
    def get(self, request, pk):
        try:
            resultado = Resultado.objects.get(pk=pk)
            serializer = ResultadoSerializer(resultado)
            return Response({'data':serializer.data,'success':True,'message':'Resultado encontrado'},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'data':[],'success':False,'message':'ERROR '+str(e)},status=status.HTTP_404_NOT_FOUND)
    #actulizar
    def put(self, request, pk):
        try:
            resultado = Resultado.objects.get(pk=pk)
        except resultado.DoesNotExist:
            return Response({'data':[],'success':False,'message':'Resultado no encontrado'},status=status.HTTP_404_NOT_FOUND)

        ### TODO OK
        try:
            serializer=ResultadoSerializer(resultado,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'data':serializer.data,'success':True,'message':'Resultado actualizado exitosamente'},status=status.HTTP_200_OK)
            else:
                return Response({'data':serializer.errors,'success':False,'message':'No se puede actulizar el resultado'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'data':serializer.errors,'success':False,'message':"ERROR "+str(e)}, status=status.HTTP_400_BAD_REQUEST)
