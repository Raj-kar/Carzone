# Generated by Django 3.2.4 on 2021-06-30 04:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0007_alter_car_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 6, 30, 10, 18, 17, 419930)),
        ),
    ]
