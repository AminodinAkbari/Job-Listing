# Generated by Django 4.0.3 on 2022-05-12 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Employer', '0046_alter_advertisement_expired_in_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisement',
            name='generate_in',
            field=models.DateField(blank=True, null=True, verbose_name='تاریخ ایجاد'),
        ),
    ]
