# Generated by Django 4.0.3 on 2022-05-08 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Controllers', '0002_languages'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=35, verbose_name='نام تگ')),
            ],
        ),
    ]
