# Generated by Django 4.0.5 on 2022-06-23 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grid', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='visit',
            name='slug',
            field=models.SlugField(default=1, unique=True),
            preserve_default=False,
        ),
    ]
