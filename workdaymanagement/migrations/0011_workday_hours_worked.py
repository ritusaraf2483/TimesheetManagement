# Generated by Django 4.0.2 on 2022-02-12 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workdaymanagement', '0010_remove_workday_hours_worked'),
    ]

    operations = [
        migrations.AddField(
            model_name='workday',
            name='hours_worked',
            field=models.TimeField(blank=True, null=True),
        ),
    ]