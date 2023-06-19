# Generated by Django 4.0.4 on 2022-09-09 11:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Controllers', '0005_states_iran'),
        ('Employer', '0040_alter_advertisement_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisement',
            name='location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Controllers.states_iran', verbose_name='شهر یا استان'),
        ),
    ]