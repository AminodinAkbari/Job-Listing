from django.http import HttpResponse

from . import serializers
from Employer import models
from rest_framework import generics , status

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

from Rest_API.permissions import IsAdManager , IsSuperUser
from Rest_API.serializers import AllManagerFullSerializer

class EmployerDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.AllManagerFullSerializer
    queryset = models.Manager.objects.all()
    permission_classes = [(IsSuperUser),]

# See And Update
"""THIS POST METHOD CAN ADD DUPLICATED EMAIL IN EMPLOYERS MODEL"""
class AllManagers(APIView):
    def get (self , request):
        obj = models.Manager.objects.all()
        data = serializers.AllManagerFullSerializer(obj , many = True).data
        return Response(data)

    def post(self , request):
        serializer = serializers.AllManagerFullSerializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return Response(serializer.data , status=status.HTTP_201_CREATED)

class RetriveManager(APIView):

    def get (self , request,pk):
        obj = models.Manager.objects.get(id=pk)
        data = serializers.AllManagerFullSerializer(obj).data
        return Response(data)

    def patch(self , request , pk):
        qs = models.Manager.objects.get(id = pk)
        serializer = AllManagerFullSerializer(qs , data= request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data)

    def delete(self , request , pk):
        qs = models.Manager.objects.get(id = pk)
        qs.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)


class AllManagers_GEN(generics.ListCreateAPIView):
    queryset = models.Manager.objects.all()
    serializer_class = serializers.AllManagerFullSerializer

class RetriveManager_GEN(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Manager.objects.all()
    serializer_class = serializers.AllManagerFullSerializer

@api_view(['GET' , 'POST'])
def all_managers_FBV_list(request):

    if request.method == 'GET':
        qs = models.Manager.objects.all()
        serializer = AllManagerFullSerializer(qs , many = True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = AllManagerFullSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

@api_view(['GET','PATCH','DELETE'])
def all_managers_FBV_detail(request , pk):

    try:
        qs = models.Manager.objects.get(id = pk)
    except:
        return Response(status=404)

    if request.method == 'GET':
        serializer = AllManagerFullSerializer(qs)
        return Response(serializer.data)

    elif request.method == 'PATCH':
        serializer = AllManagerFullSerializer(qs , data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        qs.delete()
        return Response(status = 204)
