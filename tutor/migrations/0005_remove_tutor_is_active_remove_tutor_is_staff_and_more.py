# Generated by Django 4.1 on 2022-08-06 17:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tutor', '0004_tutor_is_active_tutor_is_staff_tutor_last_login'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tutor',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='tutor',
            name='is_staff',
        ),
        migrations.RemoveField(
            model_name='tutor',
            name='last_login',
        ),
    ]
