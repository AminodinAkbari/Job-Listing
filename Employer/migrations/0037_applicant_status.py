# Generated by Django 4.0.3 on 2022-05-09 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Employer', '0036_remove_applicant_comment_remove_applicant_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicant',
            name='status',
            field=models.CharField(choices=[('send', 'در انتظار تأیین وضعیت'), ('seen', 'توسط کارفرما ماشهده شد'), ('accepted', 'تأیید برای مساحبه'), ('rejected', 'رد شده')], default='send', max_length=15),
        ),
    ]
