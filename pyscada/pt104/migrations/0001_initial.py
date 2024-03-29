# -*- coding: utf-8 -*-
# Generated by Django 1.11.25 on 2019-11-05 09:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pyscada', '0056_auto_20190625_1823'),
    ]

    operations = [
        migrations.CreateModel(
            name='PT104Device',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial_nb', models.CharField(default='', max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='PT104Variable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('channel', models.CharField(choices=[('1', 'CH1'), ('2', 'CH2'), ('3', 'CH3'), ('4', 'CH4'), ('5', 'CH5'), ('6', 'CH6'), ('7', 'CH7'), ('8', 'CH8')], default='', max_length=10)),
                ('wires', models.CharField(choices=[('2', '2 Wires'), ('3', '3 Wires'), ('4', '4 Wires')], default='', max_length=10)),
                ('data_type', models.CharField(choices=[('0', 'OFF'), ('1', 'PT100'), ('2', 'PT1000'), ('3', 'RESISTANCE_TO_375R'), ('4', 'RESISTANCE_TO_10K'), ('5', 'DIFFERENTIAL_TO_115MV'), ('6', 'DIFFERENTIAL_TO_2500MV'), ('7', 'SINGLE_ENDED_TO_115MV'), ('8', 'SINGLE_ENDED_TO_2500MV')], default='', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='ExtendedPT104Device',
            fields=[
            ],
            options={
                'verbose_name': 'PT104 Device',
                'verbose_name_plural': 'PT104 Devices',
                'proxy': True,
                'indexes': [],
            },
            bases=('pyscada.device',),
        ),
        migrations.CreateModel(
            name='ExtendedPT104Variable',
            fields=[
            ],
            options={
                'verbose_name': 'PT104 Variable',
                'verbose_name_plural': 'PT104 Variable',
                'proxy': True,
                'indexes': [],
            },
            bases=('pyscada.variable',),
        ),
        migrations.AddField(
            model_name='pt104variable',
            name='pt104_variable',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='pyscada.Variable'),
        ),
        migrations.AddField(
            model_name='pt104device',
            name='pt104_device',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='pyscada.Device'),
        ),
    ]
