# Generated by Django 4.0.2 on 2022-02-12 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workdaymanagement', '0006_alter_workday_time_in_alter_workday_time_out'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workday',
            name='hours_worked',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
