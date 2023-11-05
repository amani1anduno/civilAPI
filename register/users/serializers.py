from rest_framework import serializers
from users.models import Civilians
class CiviliansSerializer(serializers.ModelSerializer):
    class Meta:
        model=Civilians
        fields= '__all__'