# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Idlreply',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('reviewId', models.CharField(max_length=255)),
                ('authorName', models.CharField(max_length=255, null=True, blank=True)),
                ('text', models.TextField(null=True, blank=True)),
                ('seconds', models.CharField(max_length=255, null=True, blank=True)),
                ('nanos', models.IntegerField(null=True, blank=True)),
                ('starRating', models.IntegerField(null=True, blank=True)),
                ('reviewerLanguage', models.CharField(max_length=255, null=True, blank=True)),
                ('device', models.CharField(max_length=255, null=True, blank=True)),
                ('androidOsVersion', models.IntegerField(null=True, blank=True)),
                ('appVersionCode', models.IntegerField(null=True, blank=True)),
                ('appVersionName', models.CharField(max_length=255, null=True, blank=True)),
                ('thumbsUpCount', models.IntegerField(null=True, blank=True)),
                ('thumbsDownCount', models.IntegerField(null=True, blank=True)),
                ('productName', models.CharField(max_length=255, null=True, blank=True)),
                ('manufacturer', models.CharField(max_length=255, null=True, blank=True)),
                ('deviceClass', models.CharField(max_length=255, null=True, blank=True)),
                ('screenWidthPx', models.IntegerField(null=True, blank=True)),
                ('screenHeightPx', models.IntegerField(null=True, blank=True)),
                ('nativePlatform', models.CharField(max_length=255, null=True, blank=True)),
                ('screenDensityDpi', models.IntegerField(null=True, blank=True)),
                ('glEsVersion', models.IntegerField(null=True, blank=True)),
                ('cpuModel', models.CharField(max_length=255, null=True, blank=True)),
                ('cpuMake', models.CharField(max_length=255, null=True, blank=True)),
                ('ramMb', models.IntegerField(null=True, blank=True)),
                ('developertext', models.TextField(null=True, blank=True)),
                ('replyseconds', models.CharField(max_length=255, null=True, blank=True)),
            ],
        ),
    ]
