# Generated by Django 4.0.4 on 2022-06-11 16:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Employer', '0012_alter_company_manager'),
    ]

    operations = [
        migrations.RenameField(
            model_name='company',
            old_name='logo',
            new_name='profile_pic',
        ),
    ]
