from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.

@api_view(['GET'])
def welcome(request):
    return Response({'msg':'Welcome to DRF'})

class WelcomeAPIView(APIView):
    def get(self, request):
        return Response({'msg':'Welcome to DRF'})
