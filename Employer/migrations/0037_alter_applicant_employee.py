# Generated by Django 4.0.4 on 2022-09-06 08:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Employee', '0010_delete_favorite'),
        ('Employer', '0036_alter_applicant_ad_alter_applicant_employee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicant',
            name='employee',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='Employee.employeemodel'),
        ),
    ]
