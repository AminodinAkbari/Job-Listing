# Generated by Django 4.0.3 on 2022-05-12 20:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Employer', '0039_alter_advertisement_generate_in'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='advertisement',
            name='expired_in',
        ),
    ]
