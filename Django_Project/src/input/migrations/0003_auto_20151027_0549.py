# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('input', '0002_auto_20151024_2203'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='preference_1',
        ),
        migrations.AlterField(
            model_name='student',
            name='category',
            field=models.CharField(max_length=100, null=True, choices=[(b'GE', b'GE'), (b'OBC', b'OBC'), (b'SC', b'SC'), (b'ST', b'ST')]),
        ),
    ]
