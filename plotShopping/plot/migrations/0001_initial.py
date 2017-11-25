# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Age',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('labels', models.CharField(unique=True, max_length=100, verbose_name=b'\xe6\xa0\x87\xe7\xad\xbe')),
                ('data', models.IntegerField(default=0, verbose_name=b'\xe6\x95\xb0\xe6\x8d\xae')),
            ],
        ),
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('labels', models.CharField(unique=True, max_length=100, verbose_name=b'\xe6\x80\xa7\xe5\x88\xab')),
                ('data', models.IntegerField(default=0, verbose_name=b'\xe6\x95\xb0\xe6\x8d\xae')),
            ],
        ),
        migrations.CreateModel(
            name='Operate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('month', models.CharField(default=b'', unique=True, max_length=100, verbose_name=b'\xe6\x9c\x88\xe4\xbb\xbd')),
                ('click', models.IntegerField(default=0, verbose_name=b'\xe7\x82\xb9\xe5\x87\xbb\xe9\x87\x8f')),
                ('addCart', models.IntegerField(default=0, verbose_name=b'\xe5\x8a\xa0\xe5\x85\xa5\xe8\xb4\xad\xe7\x89\xa9\xe8\xbd\xa6\xe7\x9a\x84\xe9\x87\x8f')),
                ('buy', models.IntegerField(default=0, verbose_name=b'\xe8\xb4\xad\xe4\xb9\xb0\xe9\x87\x8f')),
                ('collect', models.IntegerField(default=0, verbose_name=b'\xe6\x94\xb6\xe8\x97\x8f\xe9\x87\x8f')),
            ],
        ),
    ]
