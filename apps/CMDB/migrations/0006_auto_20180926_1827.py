# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-26 10:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CMDB', '0005_auto_20180926_1736'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mysql_db',
            name='db_size',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='\u5e93\u5927\u5c0f'),
        ),
    ]
