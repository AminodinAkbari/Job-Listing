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
		self.fields['profile_pic'].widget.attrs.update({'id':'imageUpload','class':'form-control','accept':'.png, .jpg, .jpeg','type':'file'})
		self.fields['name'].widget.attrs.update({'id':'name' , 'class':'form-control'})
		self.fields['family'].widget.attrs.update({'id':'family' , 'class':'form-control'})
		self.fields['email'].widget.attrs.update({'id':'email' , 'class':'form-control'})
		self.fields['phone'].widget.attrs.update({'id':'phone' , 'class':'form-control'})
		self.fields['About'].widget.attrs.update({'id':'About' , 'class':'form-control'})
		self.fields['password'].widget.attrs.update({'id':'password' , 'class':'form-control'})
		self.fields['re_password'].widget.attrs.update({'id':'re_password' , 'class':'form-control'})

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
		email_is_exist = User.objects.filter(username = email)
		if email_is_exist is not None:
			raise forms.ValidationError('این ایمیل قبلا در سایت ثبت شده است !')
		if ('@'and'.com') not in email:
			raise ValidationError('ایمیل وارد شده معتبر نیست.')
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

	def clean_re_password(self):
		password = self.cleaned_data.get('password')
		re_password = self.cleaned_data.get('re_password')
		if len(password)<8:
			raise forms.ValidationError('کلمه عبور باید حداقل 8 کاراکتر باشد')
		if password != re_password :
			raise forms.ValidationError('کلمه های عبور با یکدیگر مغایرت دارند !')
		return password

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