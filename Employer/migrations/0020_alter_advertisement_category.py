# Generated by Django 4.0.4 on 2022-07-11 12:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Controllers', '0003_categories_icon'),
        ('Employer', '0019_alter_company_underlie'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisement',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='advertisiment', to='Controllers.categories', verbose_name='دسته بندی'),
        ),
    ]
