# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizzaMother', '0002_auto_20161012_1255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pizza',
            name='base_price',
            field=models.FloatField(default=5.0),
        ),
    ]
