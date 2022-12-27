from rest_framework import serializers
from django.contrib.auth.models import User

""" class RegistrationSerializer(serializers.ModelSerializer):

    #mapear la data
    password2=serializers.CharField(style={'input_type': 'password'},write_only=True)
    
    class Meta:
        model=User
        fields=['username','email','password','password2']
        extra_kwargs={'password': {'write_only':True}}
    def save(self):
        import pdb; pdb.set_trace()
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
            account.is_staff=self.validated_data['is_staff']
            account.save()
            return account
        except Exception as e:
            raise serializers.ValidationError({'error':'ERROR','message':str(e)}) """

############# ESTE ES EL Q FUNCIONA ##############
class UserSerializer(serializers.ModelSerializer):
    #mapear la data
    password2=serializers.CharField(style={'input_type': 'password'},write_only=True)
    class Meta:
        model = User
        fields = ('username', 'email', 'id', 'password','is_staff','password2')
        read_only_fields = ('id',)
        extra_kwargs = {
            'password': {'write_only': True}
        }
    def save(self):
        account = User(email=self.validated_data['email'],username=self.validated_data['username'])
        password = self.validated_data['password']
        account.set_password(password)
        account.is_staff=self.validated_data['is_staff']
        account.save()
        return account

    def update(self, instance, validated_data):
        instance.username=validated_data.get('username',instance.username)
        instance.email=validated_data.get('email',instance.email)
        instance.password=validated_data.get('password',instance.password)
        instance.is_staff=validated_data.get('is_staff',instance.is_staff)
        instance.save()
        return instance
"""     def delete(self, instance, validated_data):
        instance.delete()
        return instance  """