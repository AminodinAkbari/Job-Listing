# Generated by Django 4.0.3 on 2022-04-21 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Employer', '0017_advertisement_expired'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisement',
            name='expired_in',
            field=models.DateField(verbose_name='تارخ انقضای این آگهی'),
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='generate_in',
            field=models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد'),
        ),
    ]
