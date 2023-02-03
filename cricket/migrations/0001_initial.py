# Generated by Django 4.0.6 on 2022-12-03 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cricketpost',
            fields=[
                ('post_id', models.AutoField(primary_key=True, serialize=False)),
                ('PostViews', models.TextField()),
                ('category', models.CharField(choices=[('cricket', 'cricket')], default='cricket', max_length=60)),
                ('title', models.CharField(max_length=300)),
                ('author', models.CharField(max_length=50)),
                ('preContent', models.TextField()),
                ('content', models.TextField()),
                ('slug', models.CharField(default='', max_length=500)),
                ('pub_date', models.DateField()),
                ('thumbnail', models.ImageField(default='', upload_to='shop/images')),
                ('poster', models.ImageField(default='', upload_to='shop/images')),
                ('tag', models.TextField(default='post')),
            ],
        ),
    ]
