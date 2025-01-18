from rest_framework import serializers
from .models import Usuario

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['username', 'email', 'password', 'idade']
        extra_kwargs = {'password':{'write_only': True}}

    def create(self, validated_data):
        usuario = Usuario.objects.create_user(**validated_data)
        return usuario