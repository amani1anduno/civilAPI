from rest_framework import serializers
from custody.models import Custody
class CustodySerializer(serializers.ModelSerializer):
    class Meta:
        model=Custody
        fields= '__all__'