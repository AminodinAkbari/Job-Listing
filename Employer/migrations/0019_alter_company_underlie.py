# Generated by Django 4.0.4 on 2022-07-11 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Employer', '0018_alter_manager_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='underlie',
            field=models.TextField(max_length=2000, verbose_name='درباره شرکت (این متن در آگهی های شما نمایش داده می شود)'),
        ),
    ]
