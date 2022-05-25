# Generated by Django 3.0.8 on 2020-09-22 08:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0006_auto_20200922_1629'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='InitialIdentifier',
            new_name='Identifier',
        ),
        migrations.RenameField(
            model_name='specimen',
            old_name='initialIdentifer',
            new_name='identifer',
        ),
        migrations.AlterField(
            model_name='specimen',
            name='tissue',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.Tissue'),
        ),
    ]
