# Generated by Django 4.0.3 on 2022-04-21 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Employer', '0019_alter_advertisement_expired_in'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisement',
            name='expired_in',
            field=models.DateField(verbose_name='تارخ انقضای این آگهی'),
        ),
    ]
