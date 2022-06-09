# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='club_zixun',
            name='aid',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='uid',
            field=models.IntegerField(max_length=11, default=0),
        ),
    ]
