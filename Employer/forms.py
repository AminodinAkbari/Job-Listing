from django.forms import ModelForm
from django import forms
from .models import Advertisement , Company , Manager
from Employee.models import EmployeeModel
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from urllib import request

from Controllers.views import file_size

from jalali_date.fields import JalaliDateField, SplitJalaliDateTimeField
from jalali_date.widgets import AdminJalaliDateWidget, AdminSplitJalaliDateTime
# OUR New Ad Form is Down Here ↓


class EditManagerInfoForm(ModelForm):
	class Meta:
		model = Manager
		exclude= ('email',)

	def __init__(self, *args, **kwargs):
		self.user = kwargs.pop('user' , None)
		super(EditManagerInfoForm, self).__init__(*args, **kwargs)
		for field in self.fields.values():
			field.widget.attrs.update({'class': 'form-control rtl'})
			field.error_messages = {'required' : 'نمیتواند خالی باشد'}

		self.fields['profile_pic'].widget.attrs.update({'id':'imageUpload','accept':'.png, .jpg, .jpeg','type':'file'})
		self.fields['profile_pic'].validators = [file_size]

		self.fields['name'].widget.attrs.update({'id':'name'})
		self.fields['name'].required = True

		self.fields['family'].widget.attrs.update({'id':'family'})
		self.fields['family'].required = True

		self.fields['phone'].widget.attrs.update({'id':'phone'})
		self.fields['phone'].required = True

		self.fields['About'].widget.attrs.update({'id':'About'})
		self.fields['About'].required = True

	def clean_phone(self):
		phone = self.cleaned_data.get('phone')
		exist = Manager.objects.filter(phone = phone).exclude(email = self.user).exists()
		is_employee = EmployeeModel.objects.filter(phone = phone).exists()
		if exist or is_employee:
			raise forms.ValidationError('این شماره قبلا استفاده شده')
		if len(phone) < 11:
			raise forms.ValidationError('شماره تلفن نا معتبر است')
		return phone

class UpdatePasswordManagersForm(forms.Form):

	old_password = forms.CharField(widget=forms.PasswordInput,label='رمز عبور حال حاضر')
	new_password = forms.CharField(widget=forms.PasswordInput,label='رمز جدید')
	re_new_password = forms.CharField(widget=forms.PasswordInput,label='تکرار رمز جدید')

	def __init__(self , *args , **kwargs):
		self.user = kwargs.pop('user',None)
		super(UpdatePasswordManagersForm, self).__init__(*args, **kwargs)
		for field in self.fields.values():
			field.widget.attrs.update({'class': 'form-control rtl'})
			field.error_messages = {'required' : 'نمیتواند خالی باشد'}

	def clean_old_password(self):
		old_password = self.cleaned_data.get('old_password')
		new_password = self.cleaned_data.get('new_password')
		if self.user is not None:
			manager = Manager.objects.get(email = self.user.username)
			user = authenticate(request ,username = manager.email , password = old_password)
			if user is None:
				raise forms.ValidationError('رمز عبور حال حاضر اشتباه می‌باشد')
		else:
			raise forms.ValidationError('خطایی رخ داده ، اگر در حساب کاربری خود هستید یکبار خارج شوید و دوباره امتحان کنید')
		return old_password

	def clean_new_password(self):
		old_password = self.cleaned_data.get('old_password')
		new_password = self.cleaned_data.get('new_password')
		if old_password == new_password:
			raise forms.ValidationError('مقادیر رمز عبور جدید با رمز عبور قبلی نمی‌تواند یکی باشد')
		if len(new_password)<8:
			raise forms.ValidationError('کلمه عبور باید حداقل 8 کاراکتر باشد')
		return new_password

	def clean_re_new_password(self):
		new_password = self.cleaned_data.get('new_password')
		re_new_password = self.cleaned_data.get('re_new_password')
		if new_password and new_password != re_new_password :
			raise forms.ValidationError('کلمه های عبور با یکدیگر مغایرت دارند !')
		return re_new_password

class EditEmailEmployer(forms.Form):
	email = forms.EmailField(widget = forms.TextInput(attrs={'class':'form-control'}))

	def __init__(self , *args , **kwargs):
		self.user = kwargs.pop('user',None)
		super(EditEmailEmployer , self).__init__(*args , **kwargs)
		self.fields['email'].error_messages = {'invalid' : 'ایمیل معتبر نیست' , 'required' : 'نمیتواند خالی باشد'}

	def clean_email(self):
		email = self.cleaned_data.get('email')
		manager = Manager.objects.get(email = self.user.username)
		exist = Manager.objects.filter(email = email).exclude(id = manager.id).exists()
		is_employee = EmployeeModel.objects.filter(employee__username = email).exists()
		if exist or is_employee:
			raise forms.ValidationError('این ایمیل قبلا استفاده شده است')
		return email


class NewAdvertisementForm(ModelForm):
	class Meta:
		model = Advertisement
		exclude = ["generate_in" , "expired"]
	def __init__(self ,*args, **kwargs):
		user = kwargs.pop('user',None)
		super(NewAdvertisementForm, self).__init__(*args, **kwargs)
		for field in self.fields.values():
			field.widget.attrs.update({'class': 'form-control rtl'})
			field.error_messages = {'required' : 'نمی‌تواند خالی باشد'}

		self.fields['title'].widget.attrs.update({'id':'title'})
		self.fields['title'].label='عنوان آگهی'

		self.fields['location'].widget.attrs.update({'id':'location'})
		self.fields['location'].label='استان'

		self.fields['address'].widget.attrs.update({'id':'address'})

		self.fields['category'].widget.attrs.update({'id':'category'})
		self.fields['category'].label='دسته بندی'

		self.fields['company'].widget.attrs.update({'id':'company'})
		self.fields['company'].label='شرکت های معتبر شما '
		self.fields['company'].queryset = Company.objects.filter(manager__email=user , valid = True)


		self.fields['text'].widget.attrs.update({'id':'text'})
		self.fields['text'].label='متن آگهی'

		self.fields['soldier_ship'].widget.attrs.update({'id':'soldier_ship'})
		self.fields['soldier_ship'].label='وضعیت خدمت'

		self.fields['skills'].widget.attrs.update({'id':'skills'})
		self.fields['skills'].label='مهارت ها (مهارت ها را با "/" از هم جدا کنید)'

		self.fields['job_nature'].widget.attrs.update({'id':'job_nature'})
		self.fields['job_nature'].label='نوع قرار داد'

		self.fields['expired_in'] = JalaliDateField(label=('این آگهی تا چه تاریخی اعتبار دارد ؟'),widget=AdminJalaliDateWidget)
		self.fields['expired_in'].error_messages = {'required' : 'میتواند خالی باشد'}

		self.fields['salary'].widget.attrs.update({'id':'salary'})
		self.fields['salary'].label='ملبغ قرارداد (ماهیانه)'

	def clean_skills(self):
		skills = self.cleaned_data.get('skills')
		skills_count = skills.split('/')
		if len(skills_count)<2:
			raise forms.ValidationError('برای شفاف بودن آگهی ، لطفا حداقل 3 مهارت اضافه کنید')
		return skills

	def clean_text(self):
		text = self.cleaned_data.get('text')
		if len(text)>1250:
			raise forms.ValidationError('لطفا متن آگهی را کوتاه تر کنید')
		if len(text)<30:
			raise forms.ValidationError('توضیحات این آگهی نمیتواند بسیار کوتاه باشد')
		return text

	def clean_title(self):
		title = self.cleaned_data.get('title')
		if len(title)<=5:
			raise forms.ValidationError('لطفا عنوان بهتری برای آگهی ایجادکنید (عنوان بسیار کوتاه است)')
		return title

class EditAdInfoForm(ModelForm):
	class Meta:
		model = Advertisement
		exclude = ["generate_in" , "expired" , "company"]
	def __init__(self,*args , **kwargs):
		super(EditAdInfoForm, self).__init__(*args, **kwargs)
		for field in self.fields.values():
			field.widget.attrs.update({'class': 'form-control rtl'})
			field.error_messages = {'required' : 'نمی‌تواند خالی باشد'}
		self.fields['expired_in'] = JalaliDateField(label=('تاریخ انقضای این آگهی'),widget=AdminJalaliDateWidget)


	def clean_skills(self):
		skills = self.cleaned_data.get('skills')
		skills_count = skills.split('/')
		if len(skills_count)<2:
			raise forms.ValidationError('برای شفافیت آگهی ، باید حداقل 2 مهارت اضافه کنید.')
		return skills

	def clean_text(self):
		text = self.cleaned_data.get('text')
		if len(text)>1250:
			raise forms.ValidationError('لطفا متن آگهی را کوتاه تر کنید')
		if len(text)<30:
			raise forms.ValidationError('توضیحات این آگهی نمیتواند بسیار کوتاه باشد')
		return text

	def clean_title(self):
		title = self.cleaned_data.get('title')
		if len(title)<5:
			raise forms.ValidationError('لطفا عنوان بهتری برای آگهی ایجادکنید (عنوان بسیار کوتاه است)')
		return title

class NewCompanyForm(forms.ModelForm):
	class Meta:
		model = Company
		fields = '__all__'
	def __init__(self,*args,**kwargs):
		super(NewCompanyForm , self).__init__(*args , **kwargs)
		for field in self.fields.values():
			field.widget.attrs.update({'class': 'form-control rtl'})
			field.error_messages = {'required': 'نمی‌تواند خالی باشد'}


class EditCompanyForm(ModelForm):
	class Meta:
		model = Company
		exclude = ('valid','manager')
	def __init__(self,*args,**kwargs):
		super(EditCompanyForm , self).__init__(*args , **kwargs)
		for field in self.fields.values():
			field.widget.attrs.update({'class': 'form-control rtl'})
