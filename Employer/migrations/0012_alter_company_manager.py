# Generated by Django 4.0.4 on 2022-06-11 15:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Employer', '0011_alter_company_manager_alter_company_valid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='manager',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Have_companies', to='Employer.manager'),
        ),
    ]
