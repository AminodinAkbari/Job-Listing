# Generated by Django 4.0.4 on 2022-09-09 12:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Controllers', '0005_states_iran'),
        ('Employee', '0011_remove_employeemodel_state'),
    ]

    operations = [
        migrations.AddField(
            model_name='employeemodel',
            name='state',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Controllers.states_iran', verbose_name='استان محل سکونت'),
        ),
    ]
