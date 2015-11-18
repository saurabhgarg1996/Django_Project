# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('input', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Allotted',
            fields=[
                ('serial', models.CharField(max_length=10, serialize=False, primary_key=True)),
                ('roll_number', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=100)),
                ('present_branch', models.CharField(max_length=100)),
                ('allotted_branch', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Stats',
            fields=[
                ('program', models.CharField(max_length=100, serialize=False, primary_key=True)),
                ('cutoff', models.CharField(max_length=10, null=True)),
                ('sanctionedStrength', models.IntegerField()),
                ('originalStrength', models.IntegerField()),
                ('finalStrength', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('roll_number', models.CharField(max_length=9, serialize=False, primary_key=True)),
                ('cpi', models.DecimalField(null=True, max_digits=4, decimal_places=2)),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='preference_1',
            field=models.CharField(default=' ', max_length=100, choices=[(b'None', b'None'), (b'AE B.Tech', b'Aerospace Engineering B.Tech'), (b'CL B.Tech', b'Chemical Engineering B.Tech'), (b'CL Dual Deg', b'Chemical Engineering Dual Degree'), (b'CH', b'Chemistry'), (b'CE B.Tech', b'Civil Engineering B.Tech'), (b'CS B.Tech', b'Computer Science and Engineering B.Tech'), (b'EE B.Tech', b'Electrical Engineering B.Tech'), (b'EE Dual Deg E1', b'Electrical Engineering Dual Degree E1'), (b'EE Dual Deg E2', b'Electrical Engineering Dual Degree E2'), (b'EN Dual Deg', b'Energy Science and Engineering Dual Degree'), (b'EP B.Tech', b'Engineering Physics B.Tech'), (b'EP Dual Deg N1', b'Engineering Physics Dual Degree N1'), (b'ME B.Tech', b'Mechanical Engineering B.Tech'), (b'ME Dual Deg M2', b'Mechanical Engineering Dual Degree M2'), (b'MM B.Tech', b'Metallurgical Engineering B.Tech'), (b'MM Dual Deg Y1', b'Metallurgical Engineering Dual Degree Y1'), (b'MM Dual Deg Y2', b'Metallurgical Engineering Dual Degree Y2')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='preference_10',
            field=models.CharField(default=' ', max_length=100, choices=[(b'None', b'None'), (b'AE B.Tech', b'Aerospace Engineering B.Tech'), (b'CL B.Tech', b'Chemical Engineering B.Tech'), (b'CL Dual Deg', b'Chemical Engineering Dual Degree'), (b'CH', b'Chemistry'), (b'CE B.Tech', b'Civil Engineering B.Tech'), (b'CS B.Tech', b'Computer Science and Engineering B.Tech'), (b'EE B.Tech', b'Electrical Engineering B.Tech'), (b'EE Dual Deg E1', b'Electrical Engineering Dual Degree E1'), (b'EE Dual Deg E2', b'Electrical Engineering Dual Degree E2'), (b'EN Dual Deg', b'Energy Science and Engineering Dual Degree'), (b'EP B.Tech', b'Engineering Physics B.Tech'), (b'EP Dual Deg N1', b'Engineering Physics Dual Degree N1'), (b'ME B.Tech', b'Mechanical Engineering B.Tech'), (b'ME Dual Deg M2', b'Mechanical Engineering Dual Degree M2'), (b'MM B.Tech', b'Metallurgical Engineering B.Tech'), (b'MM Dual Deg Y1', b'Metallurgical Engineering Dual Degree Y1'), (b'MM Dual Deg Y2', b'Metallurgical Engineering Dual Degree Y2')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='preference_11',
            field=models.CharField(default=' ', max_length=100, choices=[(b'None', b'None'), (b'AE B.Tech', b'Aerospace Engineering B.Tech'), (b'CL B.Tech', b'Chemical Engineering B.Tech'), (b'CL Dual Deg', b'Chemical Engineering Dual Degree'), (b'CH', b'Chemistry'), (b'CE B.Tech', b'Civil Engineering B.Tech'), (b'CS B.Tech', b'Computer Science and Engineering B.Tech'), (b'EE B.Tech', b'Electrical Engineering B.Tech'), (b'EE Dual Deg E1', b'Electrical Engineering Dual Degree E1'), (b'EE Dual Deg E2', b'Electrical Engineering Dual Degree E2'), (b'EN Dual Deg', b'Energy Science and Engineering Dual Degree'), (b'EP B.Tech', b'Engineering Physics B.Tech'), (b'EP Dual Deg N1', b'Engineering Physics Dual Degree N1'), (b'ME B.Tech', b'Mechanical Engineering B.Tech'), (b'ME Dual Deg M2', b'Mechanical Engineering Dual Degree M2'), (b'MM B.Tech', b'Metallurgical Engineering B.Tech'), (b'MM Dual Deg Y1', b'Metallurgical Engineering Dual Degree Y1'), (b'MM Dual Deg Y2', b'Metallurgical Engineering Dual Degree Y2')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='preference_12',
            field=models.CharField(default=' ', max_length=100, choices=[(b'None', b'None'), (b'AE B.Tech', b'Aerospace Engineering B.Tech'), (b'CL B.Tech', b'Chemical Engineering B.Tech'), (b'CL Dual Deg', b'Chemical Engineering Dual Degree'), (b'CH', b'Chemistry'), (b'CE B.Tech', b'Civil Engineering B.Tech'), (b'CS B.Tech', b'Computer Science and Engineering B.Tech'), (b'EE B.Tech', b'Electrical Engineering B.Tech'), (b'EE Dual Deg E1', b'Electrical Engineering Dual Degree E1'), (b'EE Dual Deg E2', b'Electrical Engineering Dual Degree E2'), (b'EN Dual Deg', b'Energy Science and Engineering Dual Degree'), (b'EP B.Tech', b'Engineering Physics B.Tech'), (b'EP Dual Deg N1', b'Engineering Physics Dual Degree N1'), (b'ME B.Tech', b'Mechanical Engineering B.Tech'), (b'ME Dual Deg M2', b'Mechanical Engineering Dual Degree M2'), (b'MM B.Tech', b'Metallurgical Engineering B.Tech'), (b'MM Dual Deg Y1', b'Metallurgical Engineering Dual Degree Y1'), (b'MM Dual Deg Y2', b'Metallurgical Engineering Dual Degree Y2')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='preference_13',
            field=models.CharField(default=' ', max_length=100, choices=[(b'None', b'None'), (b'AE B.Tech', b'Aerospace Engineering B.Tech'), (b'CL B.Tech', b'Chemical Engineering B.Tech'), (b'CL Dual Deg', b'Chemical Engineering Dual Degree'), (b'CH', b'Chemistry'), (b'CE B.Tech', b'Civil Engineering B.Tech'), (b'CS B.Tech', b'Computer Science and Engineering B.Tech'), (b'EE B.Tech', b'Electrical Engineering B.Tech'), (b'EE Dual Deg E1', b'Electrical Engineering Dual Degree E1'), (b'EE Dual Deg E2', b'Electrical Engineering Dual Degree E2'), (b'EN Dual Deg', b'Energy Science and Engineering Dual Degree'), (b'EP B.Tech', b'Engineering Physics B.Tech'), (b'EP Dual Deg N1', b'Engineering Physics Dual Degree N1'), (b'ME B.Tech', b'Mechanical Engineering B.Tech'), (b'ME Dual Deg M2', b'Mechanical Engineering Dual Degree M2'), (b'MM B.Tech', b'Metallurgical Engineering B.Tech'), (b'MM Dual Deg Y1', b'Metallurgical Engineering Dual Degree Y1'), (b'MM Dual Deg Y2', b'Metallurgical Engineering Dual Degree Y2')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='preference_14',
            field=models.CharField(default=' ', max_length=100, choices=[(b'None', b'None'), (b'AE B.Tech', b'Aerospace Engineering B.Tech'), (b'CL B.Tech', b'Chemical Engineering B.Tech'), (b'CL Dual Deg', b'Chemical Engineering Dual Degree'), (b'CH', b'Chemistry'), (b'CE B.Tech', b'Civil Engineering B.Tech'), (b'CS B.Tech', b'Computer Science and Engineering B.Tech'), (b'EE B.Tech', b'Electrical Engineering B.Tech'), (b'EE Dual Deg E1', b'Electrical Engineering Dual Degree E1'), (b'EE Dual Deg E2', b'Electrical Engineering Dual Degree E2'), (b'EN Dual Deg', b'Energy Science and Engineering Dual Degree'), (b'EP B.Tech', b'Engineering Physics B.Tech'), (b'EP Dual Deg N1', b'Engineering Physics Dual Degree N1'), (b'ME B.Tech', b'Mechanical Engineering B.Tech'), (b'ME Dual Deg M2', b'Mechanical Engineering Dual Degree M2'), (b'MM B.Tech', b'Metallurgical Engineering B.Tech'), (b'MM Dual Deg Y1', b'Metallurgical Engineering Dual Degree Y1'), (b'MM Dual Deg Y2', b'Metallurgical Engineering Dual Degree Y2')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='preference_15',
            field=models.CharField(default=' ', max_length=100, choices=[(b'None', b'None'), (b'AE B.Tech', b'Aerospace Engineering B.Tech'), (b'CL B.Tech', b'Chemical Engineering B.Tech'), (b'CL Dual Deg', b'Chemical Engineering Dual Degree'), (b'CH', b'Chemistry'), (b'CE B.Tech', b'Civil Engineering B.Tech'), (b'CS B.Tech', b'Computer Science and Engineering B.Tech'), (b'EE B.Tech', b'Electrical Engineering B.Tech'), (b'EE Dual Deg E1', b'Electrical Engineering Dual Degree E1'), (b'EE Dual Deg E2', b'Electrical Engineering Dual Degree E2'), (b'EN Dual Deg', b'Energy Science and Engineering Dual Degree'), (b'EP B.Tech', b'Engineering Physics B.Tech'), (b'EP Dual Deg N1', b'Engineering Physics Dual Degree N1'), (b'ME B.Tech', b'Mechanical Engineering B.Tech'), (b'ME Dual Deg M2', b'Mechanical Engineering Dual Degree M2'), (b'MM B.Tech', b'Metallurgical Engineering B.Tech'), (b'MM Dual Deg Y1', b'Metallurgical Engineering Dual Degree Y1'), (b'MM Dual Deg Y2', b'Metallurgical Engineering Dual Degree Y2')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='preference_16',
            field=models.CharField(default=' ', max_length=100, choices=[(b'None', b'None'), (b'AE B.Tech', b'Aerospace Engineering B.Tech'), (b'CL B.Tech', b'Chemical Engineering B.Tech'), (b'CL Dual Deg', b'Chemical Engineering Dual Degree'), (b'CH', b'Chemistry'), (b'CE B.Tech', b'Civil Engineering B.Tech'), (b'CS B.Tech', b'Computer Science and Engineering B.Tech'), (b'EE B.Tech', b'Electrical Engineering B.Tech'), (b'EE Dual Deg E1', b'Electrical Engineering Dual Degree E1'), (b'EE Dual Deg E2', b'Electrical Engineering Dual Degree E2'), (b'EN Dual Deg', b'Energy Science and Engineering Dual Degree'), (b'EP B.Tech', b'Engineering Physics B.Tech'), (b'EP Dual Deg N1', b'Engineering Physics Dual Degree N1'), (b'ME B.Tech', b'Mechanical Engineering B.Tech'), (b'ME Dual Deg M2', b'Mechanical Engineering Dual Degree M2'), (b'MM B.Tech', b'Metallurgical Engineering B.Tech'), (b'MM Dual Deg Y1', b'Metallurgical Engineering Dual Degree Y1'), (b'MM Dual Deg Y2', b'Metallurgical Engineering Dual Degree Y2')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='preference_2',
            field=models.CharField(default=' ', max_length=100, choices=[(b'None', b'None'), (b'AE B.Tech', b'Aerospace Engineering B.Tech'), (b'CL B.Tech', b'Chemical Engineering B.Tech'), (b'CL Dual Deg', b'Chemical Engineering Dual Degree'), (b'CH', b'Chemistry'), (b'CE B.Tech', b'Civil Engineering B.Tech'), (b'CS B.Tech', b'Computer Science and Engineering B.Tech'), (b'EE B.Tech', b'Electrical Engineering B.Tech'), (b'EE Dual Deg E1', b'Electrical Engineering Dual Degree E1'), (b'EE Dual Deg E2', b'Electrical Engineering Dual Degree E2'), (b'EN Dual Deg', b'Energy Science and Engineering Dual Degree'), (b'EP B.Tech', b'Engineering Physics B.Tech'), (b'EP Dual Deg N1', b'Engineering Physics Dual Degree N1'), (b'ME B.Tech', b'Mechanical Engineering B.Tech'), (b'ME Dual Deg M2', b'Mechanical Engineering Dual Degree M2'), (b'MM B.Tech', b'Metallurgical Engineering B.Tech'), (b'MM Dual Deg Y1', b'Metallurgical Engineering Dual Degree Y1'), (b'MM Dual Deg Y2', b'Metallurgical Engineering Dual Degree Y2')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='preference_3',
            field=models.CharField(default=' ', max_length=100, choices=[(b'None', b'None'), (b'AE B.Tech', b'Aerospace Engineering B.Tech'), (b'CL B.Tech', b'Chemical Engineering B.Tech'), (b'CL Dual Deg', b'Chemical Engineering Dual Degree'), (b'CH', b'Chemistry'), (b'CE B.Tech', b'Civil Engineering B.Tech'), (b'CS B.Tech', b'Computer Science and Engineering B.Tech'), (b'EE B.Tech', b'Electrical Engineering B.Tech'), (b'EE Dual Deg E1', b'Electrical Engineering Dual Degree E1'), (b'EE Dual Deg E2', b'Electrical Engineering Dual Degree E2'), (b'EN Dual Deg', b'Energy Science and Engineering Dual Degree'), (b'EP B.Tech', b'Engineering Physics B.Tech'), (b'EP Dual Deg N1', b'Engineering Physics Dual Degree N1'), (b'ME B.Tech', b'Mechanical Engineering B.Tech'), (b'ME Dual Deg M2', b'Mechanical Engineering Dual Degree M2'), (b'MM B.Tech', b'Metallurgical Engineering B.Tech'), (b'MM Dual Deg Y1', b'Metallurgical Engineering Dual Degree Y1'), (b'MM Dual Deg Y2', b'Metallurgical Engineering Dual Degree Y2')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='preference_4',
            field=models.CharField(default=' ', max_length=100, choices=[(b'None', b'None'), (b'AE B.Tech', b'Aerospace Engineering B.Tech'), (b'CL B.Tech', b'Chemical Engineering B.Tech'), (b'CL Dual Deg', b'Chemical Engineering Dual Degree'), (b'CH', b'Chemistry'), (b'CE B.Tech', b'Civil Engineering B.Tech'), (b'CS B.Tech', b'Computer Science and Engineering B.Tech'), (b'EE B.Tech', b'Electrical Engineering B.Tech'), (b'EE Dual Deg E1', b'Electrical Engineering Dual Degree E1'), (b'EE Dual Deg E2', b'Electrical Engineering Dual Degree E2'), (b'EN Dual Deg', b'Energy Science and Engineering Dual Degree'), (b'EP B.Tech', b'Engineering Physics B.Tech'), (b'EP Dual Deg N1', b'Engineering Physics Dual Degree N1'), (b'ME B.Tech', b'Mechanical Engineering B.Tech'), (b'ME Dual Deg M2', b'Mechanical Engineering Dual Degree M2'), (b'MM B.Tech', b'Metallurgical Engineering B.Tech'), (b'MM Dual Deg Y1', b'Metallurgical Engineering Dual Degree Y1'), (b'MM Dual Deg Y2', b'Metallurgical Engineering Dual Degree Y2')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='preference_5',
            field=models.CharField(default=' ', max_length=100, choices=[(b'None', b'None'), (b'AE B.Tech', b'Aerospace Engineering B.Tech'), (b'CL B.Tech', b'Chemical Engineering B.Tech'), (b'CL Dual Deg', b'Chemical Engineering Dual Degree'), (b'CH', b'Chemistry'), (b'CE B.Tech', b'Civil Engineering B.Tech'), (b'CS B.Tech', b'Computer Science and Engineering B.Tech'), (b'EE B.Tech', b'Electrical Engineering B.Tech'), (b'EE Dual Deg E1', b'Electrical Engineering Dual Degree E1'), (b'EE Dual Deg E2', b'Electrical Engineering Dual Degree E2'), (b'EN Dual Deg', b'Energy Science and Engineering Dual Degree'), (b'EP B.Tech', b'Engineering Physics B.Tech'), (b'EP Dual Deg N1', b'Engineering Physics Dual Degree N1'), (b'ME B.Tech', b'Mechanical Engineering B.Tech'), (b'ME Dual Deg M2', b'Mechanical Engineering Dual Degree M2'), (b'MM B.Tech', b'Metallurgical Engineering B.Tech'), (b'MM Dual Deg Y1', b'Metallurgical Engineering Dual Degree Y1'), (b'MM Dual Deg Y2', b'Metallurgical Engineering Dual Degree Y2')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='preference_6',
            field=models.CharField(default=' ', max_length=100, choices=[(b'None', b'None'), (b'AE B.Tech', b'Aerospace Engineering B.Tech'), (b'CL B.Tech', b'Chemical Engineering B.Tech'), (b'CL Dual Deg', b'Chemical Engineering Dual Degree'), (b'CH', b'Chemistry'), (b'CE B.Tech', b'Civil Engineering B.Tech'), (b'CS B.Tech', b'Computer Science and Engineering B.Tech'), (b'EE B.Tech', b'Electrical Engineering B.Tech'), (b'EE Dual Deg E1', b'Electrical Engineering Dual Degree E1'), (b'EE Dual Deg E2', b'Electrical Engineering Dual Degree E2'), (b'EN Dual Deg', b'Energy Science and Engineering Dual Degree'), (b'EP B.Tech', b'Engineering Physics B.Tech'), (b'EP Dual Deg N1', b'Engineering Physics Dual Degree N1'), (b'ME B.Tech', b'Mechanical Engineering B.Tech'), (b'ME Dual Deg M2', b'Mechanical Engineering Dual Degree M2'), (b'MM B.Tech', b'Metallurgical Engineering B.Tech'), (b'MM Dual Deg Y1', b'Metallurgical Engineering Dual Degree Y1'), (b'MM Dual Deg Y2', b'Metallurgical Engineering Dual Degree Y2')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='preference_7',
            field=models.CharField(default=' ', max_length=100, choices=[(b'None', b'None'), (b'AE B.Tech', b'Aerospace Engineering B.Tech'), (b'CL B.Tech', b'Chemical Engineering B.Tech'), (b'CL Dual Deg', b'Chemical Engineering Dual Degree'), (b'CH', b'Chemistry'), (b'CE B.Tech', b'Civil Engineering B.Tech'), (b'CS B.Tech', b'Computer Science and Engineering B.Tech'), (b'EE B.Tech', b'Electrical Engineering B.Tech'), (b'EE Dual Deg E1', b'Electrical Engineering Dual Degree E1'), (b'EE Dual Deg E2', b'Electrical Engineering Dual Degree E2'), (b'EN Dual Deg', b'Energy Science and Engineering Dual Degree'), (b'EP B.Tech', b'Engineering Physics B.Tech'), (b'EP Dual Deg N1', b'Engineering Physics Dual Degree N1'), (b'ME B.Tech', b'Mechanical Engineering B.Tech'), (b'ME Dual Deg M2', b'Mechanical Engineering Dual Degree M2'), (b'MM B.Tech', b'Metallurgical Engineering B.Tech'), (b'MM Dual Deg Y1', b'Metallurgical Engineering Dual Degree Y1'), (b'MM Dual Deg Y2', b'Metallurgical Engineering Dual Degree Y2')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='preference_8',
            field=models.CharField(default=' ', max_length=100, choices=[(b'None', b'None'), (b'AE B.Tech', b'Aerospace Engineering B.Tech'), (b'CL B.Tech', b'Chemical Engineering B.Tech'), (b'CL Dual Deg', b'Chemical Engineering Dual Degree'), (b'CH', b'Chemistry'), (b'CE B.Tech', b'Civil Engineering B.Tech'), (b'CS B.Tech', b'Computer Science and Engineering B.Tech'), (b'EE B.Tech', b'Electrical Engineering B.Tech'), (b'EE Dual Deg E1', b'Electrical Engineering Dual Degree E1'), (b'EE Dual Deg E2', b'Electrical Engineering Dual Degree E2'), (b'EN Dual Deg', b'Energy Science and Engineering Dual Degree'), (b'EP B.Tech', b'Engineering Physics B.Tech'), (b'EP Dual Deg N1', b'Engineering Physics Dual Degree N1'), (b'ME B.Tech', b'Mechanical Engineering B.Tech'), (b'ME Dual Deg M2', b'Mechanical Engineering Dual Degree M2'), (b'MM B.Tech', b'Metallurgical Engineering B.Tech'), (b'MM Dual Deg Y1', b'Metallurgical Engineering Dual Degree Y1'), (b'MM Dual Deg Y2', b'Metallurgical Engineering Dual Degree Y2')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='preference_9',
            field=models.CharField(default=' ', max_length=100, choices=[(b'None', b'None'), (b'AE B.Tech', b'Aerospace Engineering B.Tech'), (b'CL B.Tech', b'Chemical Engineering B.Tech'), (b'CL Dual Deg', b'Chemical Engineering Dual Degree'), (b'CH', b'Chemistry'), (b'CE B.Tech', b'Civil Engineering B.Tech'), (b'CS B.Tech', b'Computer Science and Engineering B.Tech'), (b'EE B.Tech', b'Electrical Engineering B.Tech'), (b'EE Dual Deg E1', b'Electrical Engineering Dual Degree E1'), (b'EE Dual Deg E2', b'Electrical Engineering Dual Degree E2'), (b'EN Dual Deg', b'Energy Science and Engineering Dual Degree'), (b'EP B.Tech', b'Engineering Physics B.Tech'), (b'EP Dual Deg N1', b'Engineering Physics Dual Degree N1'), (b'ME B.Tech', b'Mechanical Engineering B.Tech'), (b'ME Dual Deg M2', b'Mechanical Engineering Dual Degree M2'), (b'MM B.Tech', b'Metallurgical Engineering B.Tech'), (b'MM Dual Deg Y1', b'Metallurgical Engineering Dual Degree Y1'), (b'MM Dual Deg Y2', b'Metallurgical Engineering Dual Degree Y2')]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='student',
            name='present_branch',
            field=models.CharField(default=' ', max_length=100, choices=[(b'None', b'None'), (b'AE B.Tech', b'Aerospace Engineering B.Tech'), (b'CL B.Tech', b'Chemical Engineering B.Tech'), (b'CL Dual Deg', b'Chemical Engineering Dual Degree'), (b'CH', b'Chemistry'), (b'CE B.Tech', b'Civil Engineering B.Tech'), (b'CS B.Tech', b'Computer Science and Engineering B.Tech'), (b'EE B.Tech', b'Electrical Engineering B.Tech'), (b'EE Dual Deg E1', b'Electrical Engineering Dual Degree E1'), (b'EE Dual Deg E2', b'Electrical Engineering Dual Degree E2'), (b'EN Dual Deg', b'Energy Science and Engineering Dual Degree'), (b'EP B.Tech', b'Engineering Physics B.Tech'), (b'EP Dual Deg N1', b'Engineering Physics Dual Degree N1'), (b'ME B.Tech', b'Mechanical Engineering B.Tech'), (b'ME Dual Deg M2', b'Mechanical Engineering Dual Degree M2'), (b'MM B.Tech', b'Metallurgical Engineering B.Tech'), (b'MM Dual Deg Y1', b'Metallurgical Engineering Dual Degree Y1'), (b'MM Dual Deg Y2', b'Metallurgical Engineering Dual Degree Y2')]),
            preserve_default=False,
        ),
    ]
