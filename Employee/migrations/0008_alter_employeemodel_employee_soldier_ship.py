# Generated by Django 4.0.3 on 2022-05-08 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Employee', '0007_alter_employeemodel_languages'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeemodel',
            name='employee_soldier_ship',
            field=models.CharField(blank=True, choices=[('A', 'کارت پایان خدمت'), ('B', 'معافیت تحصیلی'), ('C', 'معافیت دائم'), ('D', 'مشمول')], max_length=25, null=True, verbose_name='وضعیت نظام وظیفه (اگر خانم هستید نیاز به انتخاب گزینه نیست)'),
        ),
    ]
