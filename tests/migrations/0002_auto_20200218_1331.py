# Generated by Django 2.2.10 on 2020-02-18 13:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('concrete', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ResetPasswordToken',
            new_name='PasswordChangeToken',
        ),
        migrations.RemoveField(
            model_name='user',
            name='password_modification_token',
        ),
    ]