# Generated by Django 4.0.3 on 2022-04-17 05:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Controllers', '0001_initial'),
        ('Employer', '0006_remove_advertisement_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertisement',
            name='category',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='Controllers.categories', verbose_name='دسته بندی'),
        ),
    ]
