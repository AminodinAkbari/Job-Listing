# Generated by Django 4.0.4 on 2022-06-15 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Site_settings', '0005_remove_sociallinks_icon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sociallinks',
            name='name',
            field=models.CharField(max_length=100, verbose_name='نام به لاتین (مثلا instagram)'),
        ),
    ]
