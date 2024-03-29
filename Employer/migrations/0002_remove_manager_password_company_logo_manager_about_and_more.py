# Generated by Django 4.0.4 on 2022-05-27 19:14

import Employer.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Controllers', '0002_languages_tags'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Employer', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='manager',
            name='password',
        ),
        migrations.AddField(
            model_name='company',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to=Employer.models.upload_logo_path),
        ),
        migrations.AddField(
            model_name='manager',
            name='About',
            field=models.TextField(default='test', verbose_name='درباره شما '),
        ),
        migrations.AddField(
            model_name='manager',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to=Employer.models.upload_image_path),
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='category',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='advertisiment', to='Controllers.categories', verbose_name='دسته بندی'),
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='company', to='Employer.company', verbose_name='مربوط به شرکت'),
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='expired',
            field=models.BooleanField(default=False, verbose_name='این آگهی منقضی شده'),
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='expired_in',
            field=models.DateTimeField(blank=True, null=True, verbose_name='تارخ انقضای این آگهی'),
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='generate_in',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='تاریخ ایجاد'),
        ),
        migrations.AlterField(
            model_name='company',
            name='manager',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='Have_companies', to='Employer.manager'),
        ),
        migrations.AlterField(
            model_name='company',
            name='underlie',
            field=models.TextField(verbose_name='درباره شرکت (این متن در آگهی های شما نمایش داده می شود)'),
        ),
        migrations.CreateModel(
            name='Applicant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.CharField(choices=[('send', 'در انتظار تأیین وضعیت'), ('seen', 'توسط کارفرما مشاهده شد'), ('accepted', 'تأیید برای مصاحبه'), ('rejected', 'رد شده')], default='send', max_length=15)),
                ('ad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applicants', to='Employer.advertisement')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
