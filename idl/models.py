#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author: 陈二狗



# Create your models here.
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


class Idlreply(models.Model):
    reviewId = models.CharField(max_length=255)
    authorName = models.CharField(max_length=255, blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    seconds = models.CharField(max_length=255, blank=True, null=True)
    nanos = models.IntegerField(blank=True, null=True)
    starRating = models.IntegerField(blank=True, null=True)
    reviewerLanguage = models.CharField(max_length=255, blank=True, null=True)
    device = models.CharField(max_length=255, blank=True, null=True)
    androidOsVersion = models.IntegerField(blank=True, null=True)
    appVersionCode = models.IntegerField(blank=True, null=True)
    appVersionName = models.CharField(max_length=255, blank=True, null=True)
    thumbsUpCount = models.IntegerField(blank=True, null=True)
    thumbsDownCount = models.IntegerField(blank=True, null=True)
    productName = models.CharField(max_length=255, blank=True, null=True)
    manufacturer = models.CharField(max_length=255, blank=True, null=True)
    deviceClass = models.CharField(max_length=255, blank=True, null=True)
    screenWidthPx = models.IntegerField(blank=True, null=True)
    screenHeightPx = models.IntegerField(blank=True, null=True)
    nativePlatform = models.CharField(max_length=255, blank=True, null=True)
    screenDensityDpi = models.IntegerField(blank=True, null=True)
    glEsVersion = models.IntegerField(blank=True, null=True)
    cpuModel = models.CharField(max_length=255, blank=True, null=True)
    cpuMake = models.CharField(max_length=255, blank=True, null=True)
    ramMb = models.IntegerField(blank=True, null=True)
    developertext = models.TextField(blank=True, null=True)
    replyseconds = models.CharField(max_length=255, blank=True, null=True)
    time = models.CharField(max_length=255, blank=True, null=True)
