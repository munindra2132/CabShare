# Generated by Django 2.2.8 on 2020-08-07 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip',
            name='slug',
            field=models.SlugField(default='test-trip'),
            preserve_default=False,
        ),
    ]
