# Generated by Django 4.0.4 on 2022-06-15 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Footer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(upload_to='', verbose_name='لوگو')),
                ('short_text', models.CharField(max_length=130, verbose_name='متن کوتاه')),
                ('email', models.EmailField(max_length=254, verbose_name='ایمیل')),
            ],
        ),
    ]
