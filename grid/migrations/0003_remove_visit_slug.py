# Generated by Django 4.0.5 on 2022-06-27 07:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grid', '0002_visit_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='visit',
            name='slug',
        ),
    ]