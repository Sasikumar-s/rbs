# Generated by Django 3.1.2 on 2021-02-07 12:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Poultry', '0002_auto_20210207_1826'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='production',
            name='Time',
        ),
    ]
