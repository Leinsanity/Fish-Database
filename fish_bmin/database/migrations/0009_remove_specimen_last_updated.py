# Generated by Django 3.1.7 on 2021-04-20 15:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0008_auto_20201008_1632'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='specimen',
            name='last_updated',
        ),
    ]
