# Generated by Django 4.0.3 on 2022-04-25 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Employer', '0025_alter_manager_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manager',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='profile-pics'),
        ),
    ]
