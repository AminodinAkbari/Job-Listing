# Generated by Django 4.0.4 on 2022-07-13 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Controllers', '0003_categories_icon'),
        ('Employee', '0007_alter_employeemodel_employee_soldier_ship'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeemodel',
            name='languages',
            field=models.ManyToManyField(blank=True, to='Controllers.languages', verbose_name='زبانهای گفتاری مسلط'),
        ),
    ]
