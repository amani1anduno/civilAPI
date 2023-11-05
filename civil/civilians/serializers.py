from rest_framework import serializers
from civilians.models import Civilians
class CiviliansSerializer(serializers.ModelSerializer):
    class Meta:
        model=Civilians
        fields= '__all__'