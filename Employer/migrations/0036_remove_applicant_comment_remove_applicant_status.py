# Generated by Django 4.0.3 on 2022-05-08 15:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Employer', '0035_applicant'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='applicant',
            name='comment',
        ),
        migrations.RemoveField(
            model_name='applicant',
            name='status',
        ),
    ]
