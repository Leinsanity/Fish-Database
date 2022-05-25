# Generated by Django 3.1.7 on 2022-04-19 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0009_remove_specimen_last_updated'),
    ]

    operations = [
        migrations.CreateModel(
            name='Results',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('initial', models.CharField(default='', max_length=50)),
                ('collection_code', models.CharField(max_length=50, unique=True)),
                ('identity', models.CharField(max_length=50)),
            ],
        ),
    ]