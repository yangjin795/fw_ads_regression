# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0003_testresult_user_run'),
    ]

    operations = [
        migrations.AddField(
            model_name='testresult',
            name='name',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
