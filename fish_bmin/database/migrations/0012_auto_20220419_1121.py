# Generated by Django 3.1.7 on 2022-04-19 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0011_auto_20220419_1051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='results',
            name='collection_code',
            field=models.CharField(max_length=50),
        ),
    ]