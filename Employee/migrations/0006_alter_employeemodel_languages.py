# Generated by Django 4.0.3 on 2022-05-07 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Controllers', '0002_languages'),
        ('Employee', '0005_remove_employeemodel_languages_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeemodel',
            name='languages',
            field=models.ManyToManyField(to='Controllers.languages'),
        ),
    ]
