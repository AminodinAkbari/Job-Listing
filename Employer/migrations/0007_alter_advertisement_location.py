# Generated by Django 4.0.4 on 2022-05-30 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Employer', '0006_advertisement_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisement',
            name='location',
            field=models.CharField(choices=[('Tehran', 'تهران'), ('Shiraz', 'شیراز')], max_length=100, verbose_name='شهر یا استان'),
        ),
    ]
