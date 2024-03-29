# Generated by Django 4.0.4 on 2022-05-27 19:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Controllers', '0002_languages_tags'),
        ('Employer', '0002_remove_manager_password_company_logo_manager_about_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Employee', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employeemodel',
            name='birth',
        ),
        migrations.AddField(
            model_name='employeemodel',
            name='employee_soldier_ship',
            field=models.CharField(blank=True, choices=[('A', 'کارت پایان خدمت'), ('B', 'معافیت تحصیلی'), ('C', 'معافیت دائم'), ('D', 'مشمول')], max_length=25, null=True, verbose_name='وضعیت نظام وظیفه (اگر خانم هستید نیاز به انتخاب گزینه نیست)'),
        ),
        migrations.AddField(
            model_name='employeemodel',
            name='languages',
            field=models.ManyToManyField(to='Controllers.languages', verbose_name='زبانهای گفتاری مسلط'),
        ),
        migrations.AlterField(
            model_name='employeemodel',
            name='address',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='آدرس'),
        ),
        migrations.AlterField(
            model_name='employeemodel',
            name='employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employee', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='employeemodel',
            name='marital_status',
            field=models.CharField(blank=True, choices=[('Married', 'متأهل'), ('Single', 'مجرد')], max_length=10, null=True, verbose_name='وضعیت تأهل'),
        ),
        migrations.AlterField(
            model_name='employeemodel',
            name='phone',
            field=models.CharField(blank=True, max_length=11, null=True, verbose_name='تلفن'),
        ),
        migrations.AlterField(
            model_name='employeemodel',
            name='sex',
            field=models.CharField(blank=True, choices=[('Male', 'مرد'), ('Female', 'زن')], max_length=10, null=True, verbose_name='جنسیت'),
        ),
        migrations.AlterField(
            model_name='employeemodel',
            name='skills',
            field=models.TextField(blank=True, null=True, verbose_name='مهارت ها (مهارتهای خود را با "/ یا ،" از هم جدا کنید'),
        ),
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Employer.advertisement')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
