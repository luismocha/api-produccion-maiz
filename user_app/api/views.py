from rest_framework.decorators import api_view
from rest_framework.response import Response
from user_app.api.serializers import UserSerializer, UserSerializer
from rest_framework import serializers
from user_app import models
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.contrib.auth import get_user_model

@api_view(['GET'])
def listar_usuarios_view(request):
    print("**  LISTAR TODO LOS USUARIOS *****")
    print(request)
    try:
        print(request.user)
        if request.method == 'GET':
            ##
            User = get_user_model()
            users = User.objects.all()
            serializer =UserSerializer(users)
            print("****************TODOS LOS USUARIOS ")
            print(users)
            print("****************TODOS LOS USUARIOS SERIALIZADOS")
            print(serializer)
            return Response({'data':serializer.data,'success':True,'message':'Listado de todos los usuarios'},status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'data':[],'success':False,'message':str(e)},status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def logout_view(request):
    print("**  CERRAR SESION USER *****")
    print(request)
    try:
        print(request.user)
        if request.method == 'POST':
            request.user.auth_token.delete()
            return Response(status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error':'ERROR','message':str(e)}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def registration_view(request):
    try:
        print(" ** REGISTRAR USUARIO ***+")
        print(request.data)
        if request.method == 'POST':
            serializer=UserSerializer(data=request.data)
            data={}
            if serializer.is_valid():
                account=serializer.save()
                print("USUARIO")
                print(account)
                data['response']='El registro del usuario fue exitoso'
                data['username']=account.username
                data['email']=account.email
                token=Token.objects.get(user=account).key
                data['token']=token
                return Response(data,status=status.HTTP_200_OK)
            else:
                data=serializer.errors
                return Response(data, status=status.HTTP_400_BAD_REQUEST)
            #return Response(data)
    except Exception as e:
        return Response({'error':'ERROR','message':str(e)}, status=status.HTTP_400_BAD_REQUEST)
      