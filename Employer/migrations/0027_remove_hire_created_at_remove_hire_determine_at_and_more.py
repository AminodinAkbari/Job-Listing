# Generated by Django 4.0.4 on 2022-08-13 07:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Employer', '0026_hire_determine_at_hire_seen_at_alter_hire_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hire',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='hire',
            name='determine_at',
        ),
        migrations.RemoveField(
            model_name='hire',
            name='seen_at',
        ),
        migrations.AddField(
            model_name='applicant',
            name='determine_at',
            field=models.DateTimeField(null=True, verbose_name='تأیین وضعیت در تاریخ'),
        ),
        migrations.AddField(
            model_name='applicant',
            name='seen_at',
            field=models.DateTimeField(null=True, verbose_name='مشاهده شده توسط کارفرما'),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='تاریخ ارسال درخواست'),
        ),
    ]
