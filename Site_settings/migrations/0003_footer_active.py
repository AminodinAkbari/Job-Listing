# Generated by Django 4.0.4 on 2022-06-15 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Site_settings', '0002_alter_footer_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='footer',
            name='active',
            field=models.BooleanField(default=False, verbose_name='فعال'),
        ),
    ]