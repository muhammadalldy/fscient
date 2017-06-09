# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-09 07:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mahasiswa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('nama', models.CharField(blank=True, default='', max_length=100)),
                ('angkatan', models.CharField(blank=True, default='', max_length=100)),
                ('noreg', models.CharField(blank=True, default='', max_length=100)),
                ('peminatan', models.CharField(blank=True, default='', max_length=100)),
            ],
            options={
                'ordering': ('created',),
            },
        ),
    ]
