# Generated by Django 4.0.5 on 2022-07-18 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HMS', '0012_alter_movement_mess_cut'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movement',
            name='in_time',
            field=models.DateTimeField(default=None),
        ),
    ]
