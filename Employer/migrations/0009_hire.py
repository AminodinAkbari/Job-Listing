# Generated by Django 4.0.4 on 2022-06-04 07:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Employer', '0008_alter_advertisement_location'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='متن پیشنهاد همکاری')),
                ('contact', models.CharField(max_length=200, verbose_name='راه ارتباطی')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.CharField(choices=[('waiting', 'هنوز توسط کارجو مشاهده نشده'), ('seen', 'مشاهده شده'), ('accepted', 'کارجو برای شما رزومه و اطلاعات تماس ارسال کرده است'), ('rejected', 'توسط کارجو رد شده است')], max_length=100, verbose_name='وضعیت')),
                ('ad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Employer.advertisement', verbose_name='آگهی')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='کاربر')),
            ],
        ),
    ]
