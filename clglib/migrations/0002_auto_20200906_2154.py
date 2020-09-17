# Generated by Django 3.0.7 on 2020-09-06 16:24

import clglib.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clglib', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrower',
            name='issuedate',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='borrower',
            name='returndate',
            field=models.DateField(default=clglib.models.get_expiry),
        ),
    ]
