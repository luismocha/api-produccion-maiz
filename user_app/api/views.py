from rest_framework.decorators import api_view
from rest_framework.response import Response
from user_app.api.serializers import RegistrationSerializer
from rest_framework import serializers
from user_app import models
from rest_framework.authtoken.models import Token
from rest_framework import status

@api_view(['POST'])
def logout_view(request):
    print("**  USER *****")
    print(request)
    print(request.user)
    try:
        if request.method == 'POST':
            request.user.auth_token.delete()
            return Response(status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error':'ERROR','message':str(e)}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def registration_view(request):
    try:
        print("xxxxxxxxxx")
        print(request.data)
        if request.method == 'POST':
            serializer=RegistrationSerializer(data=request.data)
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
      