# Generated by Django 4.0.6 on 2022-08-15 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_rename_user_tokens_user_token'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_token',
            name='subscribe',
            field=models.BooleanField(default=True),
        ),
    ]