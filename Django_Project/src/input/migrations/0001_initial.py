# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('username', models.CharField(max_length=100, null=True)),
                ('cpi', models.DecimalField(null=True, max_digits=4, decimal_places=2)),
                ('category', models.CharField(max_length=100, null=True, choices=[(b'GEN', b'GEN'), (b'OBC', b'OBC'), (b'SC', b'SC'), (b'ST', b'ST')])),
                ('roll_number', models.CharField(max_length=9, serialize=False, primary_key=True)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('present_branch', models.CharField(max_length=100, null=True, choices=[(b'AE B.Tech', b'Aerospace Engineering B.Tech'), (b'CL B.Tech', b'Chemical Engineering B.Tech'), (b'CL Dual Deg', b'Chemical Engineering Dual Degree'), (b'CH', b'Chemistry'), (b'CE B.Tech', b'Civil Engineering B.Tech'), (b'CS B.Tech', b'Computer Science and Engineering B.Tech'), (b'EE B.Tech', b'Electrical Engineering B.Tech'), (b'EE Dual Deg E1', b'Electrical Engineering Dual Degree E1'), (b'EE Dual Deg E2', b'Electrical Engineering Dual Degree E2'), (b'EN Dual Deg', b'Energy Science and Engineering Dual Degree'), (b'EP B.Tech', b'Engineering Physics B.Tech'), (b'EP Dual Deg N1', b'Engineering Physics Dual Degree N1'), (b'ME B.Tech', b'Mechanical Engineering B.Tech'), (b'ME Dual Deg M2', b'Mechanical Engineering Dual Degree M2'), (b'MM B.Tech', b'Metallurgical Engineering B.Tech'), (b'MM Dual Deg Y1', b'Metallurgical Engineering Dual Degree Y1'), (b'MM Dual Deg Y2', b'Metallurgical Engineering Dual Degree Y2')])),
            ],
        ),
    ]
