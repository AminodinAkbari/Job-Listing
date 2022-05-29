from django import forms
from .models import categories
class SearchForm(forms.Form):
	title = forms.CharField()
	category = forms.ChoiceField()
	location = forms.CharField()
