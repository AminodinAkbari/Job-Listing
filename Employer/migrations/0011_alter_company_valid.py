# Generated by Django 4.0.3 on 2022-04-19 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Employer', '0010_alter_company_underlie_alter_company_valid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='valid',
            field=models.BooleanField(verbose_name='تایید کنید این شرکت وجود خارجی دارد'),
        ),
    ]
