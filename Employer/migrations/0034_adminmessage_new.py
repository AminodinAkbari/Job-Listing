# Generated by Django 4.0.4 on 2022-08-27 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Employer', '0033_adminmessage'),
    ]

    operations = [
        migrations.AddField(
            model_name='adminmessage',
            name='new',
            field=models.BooleanField(default=True),
        ),
    ]
