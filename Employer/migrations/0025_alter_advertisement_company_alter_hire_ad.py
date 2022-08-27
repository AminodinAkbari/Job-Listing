# Generated by Django 4.0.4 on 2022-08-13 06:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Employer', '0024_alter_advertisement_company'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisement',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='company', to='Employer.company', verbose_name='مربوط به شرکت'),
        ),
        migrations.AlterField(
            model_name='hire',
            name='ad',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Employer.advertisement', verbose_name='آگهی'),
        ),
    ]