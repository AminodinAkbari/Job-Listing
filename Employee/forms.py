from django import forms
from django.forms import ModelForm

from Employee.models import EmployeeModel
from Controllers.views import file_size

from jalali_date.fields import JalaliDateField
from jalali_date.widgets import AdminJalaliDateWidget
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError



from Controllers.models import *

class PersonalInfo_ResumeForm(ModelForm):
	class Meta:
		model = EmployeeModel
		fields = '__all__'

	sex = forms.ChoiceField(widget = forms.RadioSelect() ,choices =sex_types , label = 'جنسیت' ,required = False)
	marital_status = forms.ChoiceField(widget = forms.RadioSelect ,choices =marital , label = 'وضعیت تأهل' ,required = False)
	languages = forms.ModelMultipleChoiceField(queryset=Languages.objects.all(),widget=forms.CheckboxSelectMultiple ,required = False)

	def __init__(self , *args , **kwargs):
		super(PersonalInfo_ResumeForm, self).__init__(*args, **kwargs)

		self.fields['skills'].widget.attrs = {'placeholder':'تسلط به نرم افزار هلو / تسلط به زبان انگلیسی / ...' , 'rows':'9'}
		
		for field in self.fields.values():
			field.widget.attrs.update({'class': 'form-control rtl'})

		self.fields['profile_pic'] = forms.FileField(required=False, validators=[file_size])
		self.fields['employee'].disabled = True
		self.fields['sex'].widget.attrs = {'class':'rtl bb-1'}
		self.fields['marital_status'].widget.attrs = {'class':'rtl bb-1'}
		self.fields['languages'].widget.attrs = {'class':'rtl bb-1'}
		self.fields['languages'].label='به کدام زبان گفتاری مسلط هستید ؟'
		self.fields['skills'].label='مهارت های خود را بنویسید (آنها را با علامت "/" جدا کنید)'
		self.fields['birth'] = JalaliDateField(label=('تاریخ تولد'),widget=AdminJalaliDateWidget)



