# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cases', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CaseRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.CharField(max_length=50)),
                ('type', models.CharField(choices=[(b'c', b'typeC'), (b'b', b'typeB')], max_length=20)),
                ('case', models.ForeignKey(to='cases.TestCase')),
            ],
        ),
        migrations.RenameField(
            model_name='casedata',
            old_name='case_id',
            new_name='case',
        ),
    ]
