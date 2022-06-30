from rest_framework.permissions import BasePermission , SAFE_METHODS

class IsAdManager(BasePermission):
	def has_object_permission(self , request , view , obj):
		return bool(
			request.method in SAFE_METHODS or
			request.user and
			request.user.username == obj.company.manager.email
		)

class IsSuperUser(BasePermission):
	def has_permission(self , request , view):
		return bool (
		request.user.is_superuser
		)
