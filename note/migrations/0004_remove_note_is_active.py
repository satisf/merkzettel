# Generated by Django 3.0.6 on 2020-05-27 16:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0003_auto_20200527_1845'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='note',
            name='is_active',
        ),
    ]
