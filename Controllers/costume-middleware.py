from django.shortcuts import get_object_or_404
from Employer.models import Manager
from Employee.models import EmployeeModel

def define_user_type(get_response):
    def middleware(request):
        if request.user.is_authenticated and not request.user.is_superuser:
            try:
                manager = Manager.objects.filter(email = request.user.username).first()
                request.session['TYPE'] = 'Employer'
                request.session['USER_ID'] = manager.id
            except:
                employee = EmployeeModel.objects.get(employee = request.user)
                request.session['TYPE'] = 'Employee'
                request.session['USER_ID'] = employee.id
        elif request.user.is_authenticated and request.user.is_superuser:
            request.session['TYPE'] = 'SuperUser'
            request.session['USER_ID'] = request.user.id
        else:
            manager = 'Unknown'
            request.session['TYPE'] = 'Unknown'
        response = get_response(request)
        return response
    return middleware
