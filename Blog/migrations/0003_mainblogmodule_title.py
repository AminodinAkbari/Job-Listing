# Generated by Django 4.0.4 on 2022-08-14 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0002_alter_mainblogmodule_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='mainblogmodule',
            name='title',
            field=models.CharField(default='', max_length=350, verbose_name='عنوان'),
        ),
    ]
