# Generated by Django 4.0.4 on 2022-08-13 13:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Employer', '0030_alter_applicant_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicant',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='تاریخ ارسال درخواست'),
        ),
    ]