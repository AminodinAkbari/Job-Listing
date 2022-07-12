from Employer.models import Manager
from Employee.models import EmployeeModel

def define_user_type(get_response):
    def middleware(request):
        if request.user.is_authenticated:
            try:
                manager = Manager.objects.get(email = request.user.username)
                request.session['TYPE'] = 'Employer'
                request.session['Employer_ID'] = manager.id
            except:
                manager = EmployeeModel.objects.get(employee = request.user)
                request.session['TYPE'] = 'Employee'
                request.session['Employer_ID'] = manager.id
        else:
            manager = 'Unknown'
            request.session['TYPE'] = 'Unknown'

        response = get_response(request)
        return response
    return middleware
