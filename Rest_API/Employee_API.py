from rest_framework import generics , views , viewsets ,status , mixins
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from Rest_API.permissions import  OwnerCanSee

from Employee import models
from . import serializers

from django.contrib.auth.models import User

class AllEmployees(viewsets.ViewSet):
    def list(self , request):
        objs = models.EmployeeModel.objects.all()
        serializer = serializers.EmployeeModelSerializer(objs , many = True)
        return Response(serializer.data)

    def retrive(self , request , pk):
        obj = get_object_or_404(models.EmployeeModel , id = pk)
        serializer = serializers.EmployeeModelSerializer(obj)
        return Response(serializer.data)

class RegisterNewEmployee(views.APIView):
    def post(self , request):
        serializer = serializers.UserFullSerilizer(data = request.data)
        serializer.is_valid(raise_exception = True)
        user = User.objects.create_user(username = serializer.data['username'] , password = serializer.data['password'])
        models.EmployeeModel.objects.create(employee = user)
        return Response(serializer.data)

class EditEmployee(views.APIView):

    def get(self, request, pk):
        obj = get_object_or_404(User , id = pk)
        serializer = serializers.UserFullSerilizer(obj)
        return Response(serializer.data)

    def patch(self , request , pk):
        obj = get_object_or_404(User , id = pk)
        """username & password fields in User model are requirement by django default"""
        serializer = serializers.UserFullSerilizer(obj , data=request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return Response(serializer.data)

    def delete(self , request , pk):
        obj = get_object_or_404(models.EmployeeModel , id = pk)
        obj.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

class FavoriteListOnly(generics.ListAPIView):
    queryset = models.Favorite.objects.all()
    serializer_class = serializers.FavoriteModelSerializer

class FavoriteDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.FavoriteModelSerializer
    queryset = models.Favorite.objects.all()
    permission_classes = ((OwnerCanSee,))
