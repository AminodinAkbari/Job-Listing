from django.shortcuts import render

# Create your views here.

def test_seassion(request):
	request.session['test'] = 'This Is Amin'
	print(request.session['test'])
	context = {
	'test_session':request.session['test']
	}
	return render(request,'Employee/test_seassion.html')