from rest_framework import serializers
from Employer import models
from Employee import models as EMP
from django.contrib.auth.models import User

# {
# "username" : "amin",
# "password" : "aminamin2018"
# }

class UserFullSerilizer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ['username' , 'password' , 'first_name' , 'last_name']

class FavoriteModelSerializer(serializers.ModelSerializer):
	class Meta:
		model = EMP.Favorite
		fields = '__all__'

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
		fields = ['id','title' , 'expired_in' , 'category']

class ApplicantFullSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Applicant
		fields = '__all__'

class HrieModelFullSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Hire
		fields = '__all__'
# END EMPLOYER serializers

class EmployeeModelSerializer(serializers.ModelSerializer):
	class Meta:
		model = EMP.EmployeeModel
		exclude = ('profile_pic',)
