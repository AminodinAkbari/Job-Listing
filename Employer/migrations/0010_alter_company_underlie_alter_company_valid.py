# Generated by Django 4.0.3 on 2022-04-19 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Employer', '0009_remove_manager_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='underlie',
            field=models.TextField(verbose_name='درباره شرکت (این متن در آگهی های شما نمایش داده می شود)'),
        ),
        migrations.AlterField(
            model_name='company',
            name='valid',
            field=models.BooleanField(default=False, verbose_name='تایید کنید این شرکت وجود خارجی دارد'),
        ),
    ]
