from django import forms
from django.forms import ModelForm

from Employee.models import EmployeeModel
from Controllers.views import file_size

from jalali_date.fields import JalaliDateField
from jalali_date.widgets import AdminJalaliDateWidget
from django.contrib.auth.models import User

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
		self.fields['birth'] = JalaliDateField(label="تاریخ تولد",
            widget=AdminJalaliDateWidget
        )


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

class EditNameOrEmailForm(forms.Form):
	first_name = forms.CharField(widget = forms.TextInput , label = 'نام')
	last_name = forms.CharField(widget = forms.TextInput , label = 'نام خانوادگی')
	username = forms.CharField(widget = forms.TextInput , label = 'ایمیل')
	def __init__(self , *args , **kwargs):
		super(EditNameOrEmailForm, self).__init__(*args, **kwargs)
		for field in self.fields.values():
			field.widget.attrs.update({'class': 'form-control rtl mb-3'})


class ChangePassword_Employee(forms.Form):

	def __init__(self , *args , **kwargs):
		super(ChangePassword_Employee, self).__init__(*args, **kwargs)
		for field in self.fields.values():
			field.widget.attrs.update({'class': 'form-control rtl mb-2'})

	old = forms.CharField(widget=forms.PasswordInput,label='رمز عبور حال حاضر')
	new = forms.CharField(widget=forms.PasswordInput,label='رمز جدید')
	re_new = forms.CharField(widget=forms.PasswordInput,label='تکرار رمز جدید')

	def clean_new(self):
		new = self.cleaned_data.get('new')
		if len(new)<8:
			raise forms.ValidationError('کلمه عبور باید حداقل 8 کاراکتر باشد')
		return new

	def clean_re_new(self):
		new = self.cleaned_data.get('new')
		re_new = self.cleaned_data.get('re_new')
		if new != re_new :
			raise forms.ValidationError('کلمه های عبور با یکدیگر مغایرت دارند !')
		return re_new
