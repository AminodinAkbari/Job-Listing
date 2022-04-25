from django.forms import ModelForm
from django import forms
from .models import Advertisement , Company , Manager

from urllib import request

from jalali_date.fields import JalaliDateField, SplitJalaliDateTimeField
from jalali_date.widgets import AdminJalaliDateWidget, AdminSplitJalaliDateTime
# OUR New Ad Form is Down Here ↓


class NewAdvertisementForm(ModelForm):
	class Meta:
		model = Advertisement
		exclude = ["generate_in" , "expired"]
	def __init__(self ,*args, **kwargs):
		user = kwargs.pop('user',None)
		super(NewAdvertisementForm, self).__init__(*args, **kwargs)

		self.fields['title'].widget.attrs.update({'id':'title' , 'class':'form-control'})
		self.fields['title'].label='عنوان آگهی'

		self.fields['location'].widget.attrs.update({'id':'location' , 'class':'form-control'})
		self.fields['location'].label='آدرس'

		self.fields['category'].widget.attrs.update({'id':'category' , 'class':'form-control'})
		self.fields['category'].label='دسته بندی'

		self.fields['company'].widget.attrs.update({'id':'company' , 'class':'form-control'})
		self.fields['company'].label='شرکت '
		self.fields['company'].queryset = Company.objects.filter(manager__email=user , valid = True)
		

		self.fields['text'].widget.attrs.update({'id':'text' , 'class':'form-control'})
		self.fields['text'].label='متن آگهی'

		self.fields['soldier_ship'].widget.attrs.update({'id':'soldier_ship' , 'class':'form-control'})
		self.fields['soldier_ship'].label='وضعیت خدمت'

		self.fields['skills'].widget.attrs.update({'id':'skills' , 'class':'form-control'})
		self.fields['skills'].label='مهارت ها (مهارت ها را با "/" از هم جدا کنید)'

		self.fields['job_nature'].widget.attrs.update({'id':'job_nature' , 'class':'form-control'})
		self.fields['job_nature'].label='نوع قرار داد'

		self.fields['expired_in'] = JalaliDateField(label=('این آگهی تا چه تاریخی اعتبار دارد ؟'),widget=AdminJalaliDateWidget)

		self.fields['salary'].widget.attrs.update({'id':'salary' , 'class':'form-control'})
		self.fields['salary'].label='ملبغ قرارداد (ماهیانه)'

	def clean_skills(self):
		skills = self.cleaned_data.get('skills')
		skills_count = skills.split('/')
		if len(skills_count)<2:
			raise forms.ValidationError('باید برای شفافیت آگهی ، حداقل 2 مهارت اضافه کنید.')
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
		if len(title)>5:
			raise forms.ValidationError('لطفا عنوان بهتری برای آگهی ایجادکنید (عنوان بسیار کوتاه است)')
		return title

class NewCompanyForm(forms.Form):
	def __init__(self ,*args, **kwargs):
		super(NewCompanyForm, self).__init__(*args, **kwargs)
		for field in self.fields.values():
			field.widget.attrs.update({'class': 'form-control rtl'})
	name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder':'','maxlength':'80'}),
        label = 'نام شرکت'
    )
	address = forms.CharField(
		widget=forms.Textarea(attrs={'placeholder':'استان تهران ، بخش غربی ، شهرک ...' ,'maxlength':'250' }),
		label = 'آدرس'
    )
	
	underlie = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder':'شرکت شما در چه زمینه های فعالیت میکند ?','maxlength':'550'}),
        label = 'درباره شرکت توضیح دهید (این متن در آگهی های شما نمایش داده خواهد شد)'
    )

		