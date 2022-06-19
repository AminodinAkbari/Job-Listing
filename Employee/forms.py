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
		self.user = kwargs.pop('user',None)
		super(PersonalInfo_ResumeForm, self).__init__(*args, **kwargs)

		self.fields['skills'].widget.attrs = {'placeholder':'تسلط به نرم افزار هلو / تسلط به زبان انگلیسی / ...' , 'rows':'9'}

		self.fields['phone'].required = True
		self.fields['phone'].error_messages = {'required': 'شماره تلفن ضروری است'}

		self.fields['sex'].required = True
		self.fields['sex'].error_messages = {'required':'لطفا جنسیت خود را مشخص کنید'}

		self.fields['marital_status'].required = True
		self.fields['marital_status'].error_messages = {'required':'لطفا وضعیت تأهل خود را مشخص کنید'}

		self.fields['employee_soldier_ship'].required = True
		self.fields['employee_soldier_ship'].error_messages = {'required':'وضعیت خدمت شما نمیتواند خالی باشد'}



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
		self.fields['birth'].required = True
		self.fields['birth'].error_messages = {'required':'تاریخ تولد الزامی است'}


	def clean_phone(self):
		phone = self.cleaned_data.get('phone')
		exist = EmployeeModel.objects.filter(phone = phone).exclude(
		employee_id = self.user.id).exists()
		if exist:
			raise forms.ValidationError('این شماره تلفن قبلا در سایت ثبت نام شده !')
		if len(phone) < 11:
			raise forms.ValidationError('شماره تلفن معتبر نیست')
		return phone

class EditNameOrEmailForm(forms.Form):
	first_name = forms.CharField(widget = forms.TextInput , label = 'نام')
	last_name = forms.CharField(widget = forms.TextInput , label = 'نام خانوادگی')
	username = forms.CharField(widget = forms.TextInput , label = 'ایمیل')
	def __init__(self , *args , **kwargs):
		super(EditNameOrEmailForm, self).__init__(*args, **kwargs)
		for field in self.fields.values():
			field.widget.attrs.update({'class': 'form-control rtl mb-3'})
			field.error_messages = {"required" : "نمیتواند خالی باشد"}


class ChangePassword_Employee(forms.Form):

	def __init__(self , *args , **kwargs):
		super(ChangePassword_Employee, self).__init__(*args, **kwargs)
		for field in self.fields.values():
			field.widget.attrs.update({'class': 'form-control rtl mb-2'})
			field.error_messages = {'required' : 'نمی تواند خالی باشد'}

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
