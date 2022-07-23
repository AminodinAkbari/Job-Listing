from rest_framework.permissions import BasePermission , SAFE_METHODS
from Employee import models as emp_models
from rest_framework.exceptions import PermissionDenied


class IsAdManager(BasePermission):
	def has_object_permission(self , request , view , obj):
		permission = bool(request.user and request.user.username == obj.company.manager.email)
		if not permission :
			raise PermissionDenied({"From Administrator" : "Only The Manager Of This AD Can Access To It !"})

class OwnerCanSee(BasePermission):
	def has_object_permission(self , request , view , obj):
		permission = bool(request.user and obj.user.id == request.user.id)
		if not permission :
			raise PermissionDenied({"From Administrator" : "Only The Current Owner Of This Favorite Model Can Access !"})

class IsSuperUser(BasePermission):
	def has_permission(self , request , view):
		return bool (
		request.user.is_superuser
		)
