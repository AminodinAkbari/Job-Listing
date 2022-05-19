from rest_framework import serializers
from Employer.models import Advertisement

class AdvertisementsFullSerializer(serializers.ModelSerializer):
	class Meta:
		model = Advertisement
		fields = '__all__'