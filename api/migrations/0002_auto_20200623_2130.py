# Generated by Django 3.0.7 on 2020-06-24 01:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='testing_data_input',
            old_name='user_id',
            new_name='session_id',
        ),
        migrations.RenameField(
            model_name='testing_data_result',
            old_name='user_id',
            new_name='session_id',
        ),
    ]