# Generated by Django 3.2.4 on 2021-07-04 08:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0012_alter_car_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 7, 4, 14, 12, 35, 647292)),
        ),
    ]
