# Generated by Django 4.0.2 on 2022-02-11 02:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usermanagement', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='doc_id',
            field=models.IntegerField(max_length=15),
        ),
    ]