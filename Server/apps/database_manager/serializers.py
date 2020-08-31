from rest_framework import serializers
from apps.database_manager.models import Users, laptop_properties


class UsersSerializers(serializers.ModelSerializer):
    last_name = serializers.CharField(required=False)

    class Meta:
        model = Users
        fields = '__all__'

class LaptopSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = laptop_properties
        fields = '__all__'