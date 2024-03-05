from rest_framework import serializers
# from .models import Usuario
# class User_Serializer(serializers.ModelSerializer):
#     class Meta:
#         model = Usuario
#         fields=('__all__')
from .models import SolicAtend
class User_Serializer(serializers.ModelSerializer):
    class Meta:
        model = SolicAtend
        fields=('__all__')