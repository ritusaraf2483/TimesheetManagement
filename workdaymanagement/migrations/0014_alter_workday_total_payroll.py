# Generated by Django 4.0.2 on 2022-02-13 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workdaymanagement', '0013_workday_total_payroll'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workday',
            name='total_payroll',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
    ]
