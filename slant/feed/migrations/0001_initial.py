# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-10 21:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tweet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('screen_name', models.CharField(default='', max_length=200, null=True)),
                ('tweet_id', models.IntegerField(null=True, unique=True)),
                ('html', models.TextField(default='', null=True)),
            ],
        ),
    ]