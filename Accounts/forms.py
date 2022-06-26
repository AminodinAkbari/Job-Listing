from django.forms import ModelForm
from Employer.models import Manager , Company
from django.contrib.auth.models import User
from django import forms
from Accounts.models import Newsletter

class RegisterForm(ModelForm):
	password = forms.CharField(widget=forms.PasswordInput,label='رمز عبور')
	re_password = forms.CharField(widget=forms.PasswordInput,label='تکرار رمز عبور')
	class Meta:
		model = Manager
		fields= '__all__'

	def __init__(self, *args, **kwargs):
		super(RegisterForm, self).__init__(*args, **kwargs)
		for field in self.fields.values():
			field.widget.attrs.update({'class': 'form-control rtl'})
			field.error_messages = {'required':'نمیتواند خالی باشد'}
		self.fields['profile_pic'].widget.attrs.update({'id':'imageUpload','accept':'.png, .jpg, .jpeg','type':'file'})
		self.fields['name'].widget.attrs.update({'id':'name'})
		self.fields['family'].widget.attrs.update({'id':'family'})
		self.fields['email'].widget.attrs.update({'id':'email'})
		self.fields['email'].error_messages={'invalid' : 'ایمیل وارد شده معتبر نیست.',}
		self.fields['phone'].widget.attrs.update({'id':'phone'})
		self.fields['About'].widget.attrs.update({'id':'About'})
		self.fields['password'].widget.attrs.update({'id':'password'})
		self.fields['re_password'].widget.attrs.update({'id':'re_password'})

	def clean_phone(self):
		phone = self.cleaned_data.get('phone')
		phone_is_exist = Manager.objects.filter(phone=phone).exists()
		if phone_is_exist:
			raise forms.ValidationError('این شماره قبلا در سایت ثبت شده است !')
		if len(phone) != 11:
			raise forms.ValidationError('شماره وارد شده صحیح نیست')
		return phone

	def clean_email(self):
		email = self.cleaned_data.get('email')
		email_is_exist = User.objects.filter(username = email).exists()
		if email_is_exist :
			raise forms.ValidationError('این ایمیل قبلا در سایت ثبت شده است !')
		return email

	def clean_re_password(self):
		password = self.cleaned_data.get('password')
		re_password = self.cleaned_data.get('re_password')
		if len(password)<8:
			raise forms.ValidationError('کلمه عبور باید حداقل 8 کاراکتر باشد')
		if password != re_password :
			raise forms.ValidationError('کلمه های عبور با یکدیگر مغایرت دارند !')
		return password


class LoginForm(forms.Form):
    username = forms.CharField(label='نام کاربری',
        widget=forms.TextInput(attrs={'class':'form-control'}),
    )
    password = forms.CharField(label='رمزعبور',
        widget=forms.PasswordInput(attrs={'class':'form-control'}),
    )


class EmployeeRegister(ModelForm):
	class Meta:
		model = User
		fields = ['first_name' , 'last_name' ,'username','password']

	re_password = forms.CharField(widget=forms.PasswordInput,label='تکرار رمز عبور')

	def __init__(self,*args , **kwargs):
		super(EmployeeRegister , self).__init__(*args , **kwargs)
		for field in self.fields.values():
			field.widget.attrs.update({'class': 'form-control rtl'})
		self.fields['first_name'].label = 'نام'
		self.fields['last_name'].label = 'نام خانوادگی'
		self.fields['username'].label = 'ایمیل'
		self.fields['password'].label = 'رمز عبور'

	def clean_re_password(self):
		password = self.cleaned_data.get('password')
		re_password = self.cleaned_data.get('re_password')
		if len(password)<8:
			raise forms.ValidationError('کلمه عبور باید حداقل 8 کاراکتر باشد')
		if password != re_password :
			raise forms.ValidationError('کلمه های عبور با یکدیگر مغایرت دارند !')
		return password

	def clean_username(self):
		email = self.cleaned_data.get('username')
		if '@' not in str(email) or '.com' not in str(email):
			raise forms.ValidationError('ایمیل معتبر نیست')
		duplicate = User.objects.filter(username = email).exists()
		if duplicate:
			raise forms.ValidationError('این ایمیل قبل در سایت ثبت نام شده است')
		return email

class NewsletterEmailsForm(forms.ModelForm):
	class Meta:
		model = Newsletter
		fields = ['email']

	def __init__(self,*args , **kwargs):
		super(NewsletterEmailsForm , self).__init__(*args , **kwargs)
		self.fields['email'].widget.attrs.update({'class':'form-control'})

	def clean_email(self):
		email = self.cleaned_data.get('email')
		All_emails = Newsletter.objects.filter(email = email).first()
		if All_emails is not None:
			raise forms.ValidationError('این ایمیل قبلا در خبرنامه ثبت نام کرده است')
		return email
