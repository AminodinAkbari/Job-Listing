from django.shortcuts import render
from Employer.models import Advertisement

from rest_framework import generics
from rest_framework.response import Response
from .serializers import AdvertisementsFullSerializer
from .permissions import IsAdManager


# Create your views here.

class All_Advertisements(generics.ListAPIView):
	queryset = Advertisement.objects.all()
	serializer_class = AdvertisementsFullSerializer

class Ads_FullMangement(generics.RetrieveUpdateDestroyAPIView):
	queryset = Advertisement.objects.all()
	serializer_class = AdvertisementsFullSerializer
	permission_classes = ((IsAdManager,))
