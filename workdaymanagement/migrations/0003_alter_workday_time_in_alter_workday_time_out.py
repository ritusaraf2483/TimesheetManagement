# Generated by Django 4.0.2 on 2022-02-11 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workdaymanagement', '0002_alter_workday_time_in_alter_workday_time_out'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workday',
            name='time_in',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='workday',
            name='time_out',
            field=models.TimeField(),
        ),
    ]
