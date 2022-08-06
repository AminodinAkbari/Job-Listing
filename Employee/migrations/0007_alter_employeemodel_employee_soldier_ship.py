# Generated by Django 4.0.4 on 2022-06-20 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Employee', '0006_alter_employeemodel_employee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeemodel',
            name='employee_soldier_ship',
            field=models.CharField(blank=True, choices=[('A', 'کارت پایان خدمت'), ('B', 'معافیت تحصیلی'), ('C', 'معافیت دائم'), ('D', 'مشمول'), ('Shes a Woman', 'شامل من نیست (مختص خانم ها)')], max_length=25, null=True, verbose_name='وضعیت نظام وظیفه (اگر خانم هستید نیاز به انتخاب گزینه نیست)'),
        ),
    ]