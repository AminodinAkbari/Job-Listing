# Generated by Django 4.0.3 on 2022-05-21 14:06

from django.db import migrations
import django_jalali.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('Employee', '0010_alter_employeemodel_employee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeemodel',
            name='birth',
            field=django_jalali.db.models.jDateField(blank=True, null=True, verbose_name='تارخ تولد'),
        ),
    ]
