from django import forms
from Employer.models import Advertisement

class SearchForm(forms.ModelForm):
	class Meta:
		model = Advertisement
		fields = ['location']

	def __init__(self ,*args, **kwargs):
		super(SearchForm, self).__init__(*args, **kwargs)
		self.fields['location'].widget.attrs.update({'id':'location' , 'class':'form-control'})
		self.fields['location'].label = ''
