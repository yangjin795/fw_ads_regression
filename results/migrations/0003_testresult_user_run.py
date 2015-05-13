# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0002_regressionuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='testresult',
            name='user_run',
            field=models.ForeignKey(default=1, to='results.RegressionUser'),
            preserve_default=False,
        ),
    ]
