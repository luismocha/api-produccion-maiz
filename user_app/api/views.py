from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from app.api.permissions import AdminAuthPutOrReadOnly, AdminOrReadOnly
from rest_framework.authtoken.models import Token
from rest_framework import status
import string
import secrets
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

from user_app.api.serializers import    UserSerializer
from django.contrib.auth import authenticate
from django.core.mail import send_mail
from proyecto.settings import EMAIL_HOST

### INCIAR SESION #####
@api_view(['POST'])
def login_view(request):
    try:
        data={}
        #import pdb; pdb.set_trace()
        #recuperamos las credenciales y autenticamos al usuarios
        usuarioName=request.data.get('username',None)
        password=request.data.get('password',None)
        userAuth=authenticate(username=usuarioName, password=password)
        ## si es correcto añadirmos a la reques la ifnroamcion de sesion
        if userAuth:
            #User = get_user_model()
            user = User.objects.get(username=usuarioName)
            data['response']='Inicio de sesión exitosamente'
            data['username']=user.username
            data['email']=user.email
            data['is_staff']=user.is_staff
            token, _ = Token.objects.get_or_create(user=userAuth)
            data['token']=token.key
            return Response({'data':data,'success':True,'message':'Inicio de sesión exitosamente'},status=status.HTTP_200_OK)
        return Response({'data':data,'success':False,'message':'Contraseña o usuario incorrecto'},status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'data':[],'success':False,'message':"ERROR "+str(e)},status=status.HTTP_404_NOT_FOUND)

### OBTENRE USUARIO POR ID Y ACTUALIZAR USUARIO POR ID
@api_view(['GET','PUT','DELETE'])
@permission_classes([AdminAuthPutOrReadOnly])
def usuario_id_view(request,pk):
    #import pdb; pdb.set_trace()
    try:
        User = get_user_model()
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response({'data':[],'success':True,'message':'Usuario no encontrado'},status=status.HTTP_404_NOT_FOUND)

    try:
        if request.method == 'GET':
            serializer =UserSerializer(user)
            return Response({'data':serializer.data,'success':True,'message':'Usuario encontrado'},status=status.HTTP_200_OK)
        
        if request.method=='PUT':
            ## para q no se cree dos veces el mismo objeto
            serializerActualizar =UserSerializer(user,data=request.data)
            if serializerActualizar.is_valid():
                count = User.objects.all().count()
                if (count==1 and request.data.get('is_staff')==False):
                    return Response({'data':[],'success':False,'message':'No puede quitar los permisos al usuario, por lo menos debe existir un usuario'},status=status.HTTP_404_NOT_FOUND)
                serializerActualizar.update(user,request.data)
                return Response({'data':serializerActualizar.data,'success':True,'message':'Usuario actualizado exitosamente'},status=status.HTTP_200_OK)
            else:
               return Response({'data':serializerActualizar.errors,'success':False,'message':'No se puede actulizar el usuario'}, status=status.HTTP_400_BAD_REQUEST)

        if request.method=='DELETE':
            serializer = UserSerializer(user)
            count = User.objects.all().count()
            if (count==1):
                return Response({'data':[],'success':False,'message':'No puede eliminar todos los usuaurios , por lo menos debe existir un usuario'},status=status.HTTP_404_NOT_FOUND)
            user.delete()
            return Response({'data':serializer.data,'success':True,'message':'Usuario elimiado exitosamente'},status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'data':[],'success':False,'message':"ERROR "+str(e)},status=status.HTTP_404_NOT_FOUND)

########## LISTAR TODOS LOS USUARIOS #########
@api_view(['GET'])
@permission_classes([AdminAuthPutOrReadOnly])
def listar_usuarios_view(request):
    try:
        print(request.user)
        if request.method == 'GET':
            User = get_user_model()
            users = User.objects.all()
            serializer =UserSerializer(users,many=True)
            return Response({'data':serializer.data,'success':True,'message':'Listado de todos los usuarios'},status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'data':[],'success':False,'message':"ERROR "+str(e)},status=status.HTTP_400_BAD_REQUEST)

## CERRAR  SESION ######
@api_view(['POST'])
def logout_view(request):
    try:
        if request.method == 'POST':
            #logout(request)
            request.user.auth_token.delete()
            return Response({'data':[],'success':True,'message':'Sesión cerrada exitosamente'},status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'data':[],'success':False,'message':"ERROR "+str(e)},status=status.HTTP_404_NOT_FOUND)



#### REGISTRAR USUARIO ########
@api_view(['POST'])
@permission_classes([AdminOrReadOnly])
def registration_view(request):
    try:
        if request.method == 'POST':
            ##valir que el usuarioname sera unico
            User = get_user_model()
            users_name = User.objects.filter(username=request.data['username']).first()
            if  users_name:
                return Response({'data':[],'success':False,'message':'Ya existe un usurio con el nombre de '+request.data['username']},status=status.HTTP_404_NOT_FOUND)
            users_email = User.objects.filter(email=request.data['email']).first()
            if  users_email:
                return Response({'data':[],'success':False,'message':'Ya existe un usurio con el correo de '+request.data['email']},status=status.HTTP_404_NOT_FOUND)
            ## TODO OKKKK
            serializer=UserSerializer(data=request.data)
            data={}
            if serializer.is_valid():
                account=serializer.save()
                data['response']='El registro del usuario fue exitoso'
                data['username']=account.username
                data['email']=account.email
                data['is_staff']=account.is_staff
                token=Token.objects.get(user=account).key
                data['token']=token
                return Response({'data':data,'success':True,'message':'Usuario creado exitosamente'},status=status.HTTP_201_CREATED)
            else:
                data=serializer.errors
                return Response({'data':data,'success':False,'message':"No se puede crear el usuario "}, status=status.HTTP_400_BAD_REQUEST)
            #return Response(data)
    except Exception as e:
        return Response({'data':[],'success':False,'message':"ERROR "+str(e)}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def recuperarContraseña(request):
    try:
        email=request.data["email"]
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        return Response({'data':[],'success':False,'message':"El usuario con el correo "+str(email)+" no existe "},status=status.HTTP_404_NOT_FOUND)
    try:
        data={}
        ##enviar correo
        passwordRANDON=''
        pwd_length = 12
        letters = string.ascii_letters
        digits = string.digits
        special_chars = string.punctuation
        alphabet = letters + digits + special_chars
        for i in range(pwd_length):
            passwordRANDON += ''.join(secrets.choice(alphabet))
        user.set_password(passwordRANDON)
        user.save()
        emailEnviado=send_mail(
            'Hola '+str(user.username)+' esta es su nueva  contraseña generado para su inicio de session ',
            'Su nueva contraseña generado para su inicio de session es : '+passwordRANDON,
            EMAIL_HOST,
            [user.email],
            fail_silently=False,
            )
        return Response({'data':emailEnviado,'success':True,'message':'Se envio nueva contraseña a su correo'},status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'data':[],'success':False,'message':"ERROR "+str(e)},status=status.HTTP_404_NOT_FOUND)