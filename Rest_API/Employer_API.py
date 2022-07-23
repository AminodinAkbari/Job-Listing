from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.mixins import CreateModelMixin
from rest_framework import generics , status

from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from . import serializers
from Employer import models

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

from Rest_API.permissions import IsAdManager , IsSuperUser
from Rest_API.serializers import AllManagerFullSerializer

"""In This File I Show My Skills with Any Method Of APIS (Functional , Class Base , APIView)"""
# Hope Its Helped

class EmployerDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.AllManagerFullSerializer
    queryset = models.Manager.objects.all()
    permission_classes = [(IsSuperUser),]

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
        obj = get_object_or_404(models.Manager,id=pk)
        data = serializers.AllManagerFullSerializer(obj).data
        return Response(data)

    def patch(self , request , pk):
        qs = get_object_or_404(models.Manager,id = pk)
        serializer = AllManagerFullSerializer(qs , data= request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data)

    def delete(self , request , pk):
        qs = get_object_or_404(models.Manager,id = pk)
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

    qs = get_object_or_404(models.Manager,id = pk)

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
        return Response(status=status.HTTP_204_NO_CONTENT)

# ----------------- Applcant Model APIs -----------------
class AllApplicants(CreateModelMixin,generics.ListAPIView):
    serializer_class = serializers.ApplicantFullSerializer
    queryset = models.Applicant.objects.all()

    def post(self , request):
        return self.create(request)

class ApplicantDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.ApplicantFullSerializer
    queryset = models.Applicant.objects.all()
# ------------------Company Model APIs------------------
class AllCompanies(CreateModelMixin,generics.ListAPIView):
    serializer_class = serializers.AllCompaniesFullSerializer
    queryset = models.Company.objects.all()
    def post(self , request):
        return self.create(request)

class CompaniesDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.AllCompaniesFullSerializer
    queryset = models.Company.objects.all()

#----------------- Advertisement Model APIs ------------------
class ALLAds(CreateModelMixin,generics.ListAPIView):
    queryset = models.Advertisement.objects.all()
    serializer_class = serializers.AdvertisementMiniSerilalzer

class ADDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.AdvertisementsFullSerializer
    queryset = models.Advertisement.objects.all()
    permission_classes = ((IsAdManager,))

#----------------- Hire Model APIs ------------------
class AllHires(CreateModelMixin,generics.ListAPIView):
    serializer_class = serializers.HrieModelFullSerializer
    queryset = models.Hire.objects.all()

    def post(self , request):
        return self.create(request)

class HireDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.HrieModelFullSerializer
    queryset = models.Hire.objects.all()
