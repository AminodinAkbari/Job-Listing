# Generated by Django 4.0.3 on 2022-04-25 17:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Employer', '0029_alter_manager_about'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='manager',
            name='family',
        ),
        migrations.RemoveField(
            model_name='manager',
            name='name',
        ),
    ]
