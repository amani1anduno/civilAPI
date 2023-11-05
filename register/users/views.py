from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from users.serializers import CiviliansSerializer
from users.models import Civilians
from django.http import JsonResponse
import requests
import json
def index(request):
    response = requests.post('http://localhost:8000/api/',json=request.POST.dict())
    return render(request,'users/signup.html' , {"response":response})
    pass

@api_view(['POST','GET'])
def send(request):
    if request.method == 'POST':
        civilians= Civilians.objects.all()
        serializer =CiviliansSerializer(civilians, many=True)
        #json_body = json_body = json.loads(request.body)bodydi
        user=request.data.copy()
        user=user.dict()
        del user["csrfmiddlewaretoken"]
        user['nin']= int(user['nin'])
        user['phone_number']= int(user['phone_number'])
        serialiser = CiviliansSerializer(data=user)
        # get the response from the URL
        userj=json.dumps(user, indent = 4)
        response = requests.post('http://localhost:8001/api',json=json.loads(userj))
        response2 = requests.post('http://localhost:8002/api',json={'nin':user["nin"]})
        response3 = requests.post('http://localhost:8003/api',json={'nin':user["nin"]})
        if response.status_code==500 or response2.status_code==500 or response3.status_code==500:
            return render(request,'users/response.html' , {"response":"we encountered an external server error"})


        total= response.json() and response2.json() and response3.json()
        #total=False
        if serialiser.is_valid() and total:
            serialiser.save()
            return render(request,'users/response.html' , {"response":"your request was save, please wait for your passport"})
        else :
            return render(request,'users/response.html' , {"response":"your information is fauty"})
    else: return render(request,'users/response.html' , {"response":"welcom to the regestration page"})