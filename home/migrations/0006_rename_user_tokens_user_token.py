# Generated by Django 4.0.6 on 2022-08-14 10:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_user_tokens'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='user_tokens',
            new_name='user_token',
        ),
    ]
