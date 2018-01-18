#!/usr/bin/env python
# -*- coding:utf8 -*-
#Author: 陈二狗
from __future__ import unicode_literals
from idl.models import Idlreply

import urllib2, urllib
import json
import time
from config import *


def get_atoken():
    f = urllib2.urlopen(
        url = url,
        data = urllib.urlencode(data)
        )
    a = f.read()
    text = json.loads(a)
    atoken = text['access_token']

    global firsttime
    firsttime = int(time.time())

    return atoken , firsttime

atoken = (get_atoken()[0])


def diff(first):
    secondtime = int(time.time())
    if secondtime - first <= 3000:
        pass
    else:
        global atoken
        atoken = (get_atoken()[0])
        return atoken
        print "heihei"

# 获取20条评论列表
def get_list():
    diff(firsttime)
    url = Scope
    textmod = {'access_token': atoken}
    textmod = urllib.urlencode(textmod)
    req = urllib2.Request(url='%s%s%s&maxResults=20' % (url, '?', textmod))
    res = urllib2.urlopen(req)
    res = res.read()
    a = json.dumps(json.loads(res), ensure_ascii=False)
    return a

dataall = get_list()
dataalljson=json.loads(dataall)

def repeat(rid):
    a = 0
    for i in Idlreply.objects.order_by('-id')[0:40]:
        if i.reviewId == rid.encode('utf-8'):
            a = 1
        else:
            a = a
    if a > 0:
        return True
    else:
        return False

def timeconversion(seconds):
    #转换int
    timestamp = int(seconds)
    #转换成localtime
    time_local = time.localtime(timestamp)
    #转换成新的时间格式
    dt = time.strftime("%Y-%m-%d %H:%M:%S",time_local)
    return dt

def savadb(data):

    comments = data['comments'][0]
    userComment = comments['userComment']
    lastModified = userComment['lastModified']
    deviceMetadata = userComment['deviceMetadata']

    onereply = Idlreply()

    if repeat(data.get('reviewId')):
        print "haha"
    else:
        onereply.reviewId = data.get('reviewId')
        onereply.authorName = data.get('authorName')
        onereply.text = userComment.get('text')
        onereply.seconds = lastModified.get('seconds')
        onereply.time = timeconversion(onereply.seconds)
        onereply.nanos = lastModified.get('nanos')
        onereply.starRating = userComment.get('starRating')
        onereply.device = userComment.get('device')
        onereply.reviewerLanguage = userComment.get('reviewerLanguage')
        onereply.androidOsVersion = userComment.get('androidOsVersion')
        onereply.appVersionCode = userComment.get('appVersionCode')
        onereply.appVersionName = userComment.get('appVersionName')
        onereply.thumbsDownCount = userComment.get('thumbsDownCount')
        onereply.thumbsUpCount = userComment.get('thumbsUpCount')
        onereply.screenDensityDpi = deviceMetadata.get('screenDensityDpi')
        onereply.screenHeightPx = deviceMetadata.get('screenHeightPx')
        onereply.screenWidthPx = deviceMetadata.get('screenWidthPx')
        onereply.cpuModel = deviceMetadata.get('cpuModel')
        onereply.productName = deviceMetadata.get('productName')
        onereply.deviceClass = deviceMetadata.get('deviceClass')
        onereply.cpuMake = deviceMetadata.get('cpuMake')
        onereply.ramMb = deviceMetadata.get('ramMb')
        onereply.manufacturer = deviceMetadata.get('manufacturer')
        onereply.nativePlatform = deviceMetadata.get('nativePlatform')
        onereply.glEsVersion = deviceMetadata.get('glEsVersion')

        onereply.save()


def main():
    for i in range(19,-1,-1):
        data = dataalljson['reviews'][i]
        savadb(data)

if __name__ == '__main__':
    main()
    print("Done!")
