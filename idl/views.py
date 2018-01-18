#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author: 陈二狗

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response
from models import Idlreply
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# def reply(request):
#     all_reply = Idlreply.objects.order_by('-id')[0:20]
#     return render_to_response("reply/replylist.html", locals())






def reply(request):
    contact_list = Idlreply.objects.order_by('-id')
    paginator = Paginator(contact_list, 15)  # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)

    return render(request, 'reply/replylist.html', {'contacts': contacts})

def reviews(request, src):
    one_reply = Idlreply.objects.get(id=src)
    return render_to_response("reply/reviews.html", locals())

def index(request):
    #all_reply = Idlreply.objects.order_by('-id')[0:30]
    return render_to_response("index.html", locals())


