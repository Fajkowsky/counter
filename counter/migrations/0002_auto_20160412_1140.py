# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('counter', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(unique=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='word',
            name='name',
            field=models.CharField(unique=True, max_length=200),
        ),
    ]
