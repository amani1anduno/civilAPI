from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from civilians.serializers import CiviliansSerializer
from civilians.models import Civilians
from django.http import JsonResponse
import requests


# Create your views here.
def vote(request):
    return HttpResponse("you are in the civil server's front and this server only offers an API so you cant interact with it" )
@api_view(['GET','POST'])
def varify(request):
    if request.method == 'GET':
        civilians= Civilians.objects.all()
        serializer =CiviliansSerializer(civilians, many=True)
        return Response(serializer.data)

    civilians= Civilians.objects.filter(nin=request.data['nin'])[:1].get()
    serializer =CiviliansSerializer(civilians, many=False)
    return Response(serializer.data==request.data)
@api_view(['POST'])
def getre(request):
    # get the response from the URL
    obj={'nin': 1234567, 'name': 'name', 'last_name': 'name', 'father_name': 'name', 'mother_name': 'name', 'mother_last_name': 'name', 'phone_number': 11111}
    response = requests.post('http://127.0.0.1:8000/civilians/api?format=json',json=request.data)
    ##result = do_something_with_response(response)
    return Response(response.json())
