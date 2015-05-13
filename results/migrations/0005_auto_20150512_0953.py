# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cases', '0001_initial'),
        ('results', '0004_testresult_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='CaseResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('case_result', models.CharField(choices=[(b'F', b'Failed'), (b'P', b'Pass'), (b'W', b'Warning')], max_length=20)),
                ('case', models.ForeignKey(to='cases.TestCase')),
            ],
        ),
        migrations.RemoveField(
            model_name='regressionuser',
            name='user',
        ),
        migrations.AddField(
            model_name='testresult',
            name='ads_revision',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='testresult',
            name='user_run',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='RegressionUser',
        ),
        migrations.AddField(
            model_name='caseresult',
            name='result',
            field=models.ForeignKey(to='results.TestResult'),
        ),
    ]
