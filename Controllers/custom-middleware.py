from Employer.models import Manager

def define_user_type(get_response):
    def middleware(request):
        if request.user.is_authenticated:
            try:
                manager = Manager.objects.get(email = request.user.username)
                request.session['TYPE'] = 'Employer'
            except:
                manager = None
                request.session['TYPE'] = 'Employee'
        else:
            manager = 'Unknown'
            request.session['TYPE'] = 'Unknown'
            
        response = get_response(request)
        return response
    return middleware
