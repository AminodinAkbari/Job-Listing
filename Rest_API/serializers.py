from rest_framework import serializers
from Employer import models

class AllManagerFullSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Manager
		fields = '__all__'

class AllCompaniesFullSerializer(serializers.ModelSerializer):
	class Meta :
		model = models.Company
		fields = '__all__'

class AdvertisementsFullSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Advertisement
		fields = '__all__'

class AdvertisementMiniSerilalzer(serializers.ModelSerializer):
	class Meta:
		model = models.Advertisement
		fields = ['title' , 'expired_in' , 'category']
