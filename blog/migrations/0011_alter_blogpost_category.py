# Generated by Django 4.0.6 on 2022-08-03 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_blogpost_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='category',
            field=models.CharField(choices=[('#you-will-love-to-know', 'You will love to know'), ('#superhero', 'SuperHero'), ('#hollywood', 'Hollywood'), ('#bollywood', 'Bollywood'), ('#anime', 'Anime')], default='you_will_love_to_know', max_length=60),
        ),
    ]
