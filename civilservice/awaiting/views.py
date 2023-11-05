from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from awaiting.serializers import CustodySerializer
from awaiting.models import Custody
from django.http import JsonResponse
import requests

# Create your views here.
# Create your views here.
@api_view(['GET','POST'])
def varify(request):
    if request.method == 'GET':
        awaitings= Custody.objects.all()
        serializer =CustodySerializer(awaitings, many=True)
        return Response(serializer.data)

    if Custody.objects.filter(nin=request.data['nin']).exists():
        return Response(False)
    else : return Response(True)