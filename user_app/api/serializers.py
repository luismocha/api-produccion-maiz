from rest_framework import serializers
from django.contrib.auth.models import User

class RegistrationSerializer(serializers.ModelSerializer):

    #mapear la data
    password2=serializers.CharField(style={'input_type': 'password'},write_only=True)
    
    class Meta:
        model=User
        fields=['username','email','password','password2']
        extra_kwargs={'password': {'write_only':True}}
    def save(self):
        try:
            password = self.validated_data['password']
            password2 = self.validated_data['password2']
            if User.objects.filter(username=self.validated_data['username']).exists():
                print("-----------ENCONTRADO USUARIO")
                raise serializers.ValidationError({'error':'El nombre de usuario ya existe'})
            else:
                print("----------NO -ENCONTRADO USUARIO")
            if password != password2:
                raise serializers.ValidationError({'error':'El password de confirmación no coincide'})
            
            if User.objects.filter(email=self.validated_data['email']).exists():
                raise serializers.ValidationError({'error':'El correo del usuario ya existe'})


            ## TOODO OK
            account = User(email=self.validated_data['email'],username=self.validated_data['username'])
            account.set_password(password)
            account.save()
            return account
        except Exception as e:
            raise serializers.ValidationError({'error':'ERROR','message':str(e)})


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'id', 'password')
        read_only_fields = ('id',)
        extra_kwargs = {
            'password': {'write_only': True}
        }
    
    def update(self, instance, validated_data):
        instance.username=validated_data.get('username',instance.username)
        instance.email=validated_data.get('email',instance.email)
        instance.password=validated_data.get('password',instance.longitud)
        instance.save()
        return instance