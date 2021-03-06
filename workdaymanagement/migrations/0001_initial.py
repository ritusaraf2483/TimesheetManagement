# Generated by Django 4.0.2 on 2022-02-11 02:27

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Payroll',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Workday',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('docid', models.IntegerField()),
                ('doctor', models.CharField(max_length=20)),
                ('sector', models.CharField(blank=True, max_length=7)),
                ('work_date', models.DateField(blank=True, default=datetime.date.today)),
                ('time_in', models.TimeField()),
                ('time_out', models.TimeField()),
                ('payroll', models.FloatField()),
                ('hours_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workdaymanagement.payroll')),
                ('location', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='workdaymanagement.location')),
            ],
        ),
    ]
