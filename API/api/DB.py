#!/usr/bin/python
# -*- coding: utf-8 -*-

from mongoengine import *

connect('sampledatabase', host='172.17.1.57', port=7777)

class Record(Document):
    title        = StringField(max_length=128, required=True)
    description  = StringField()
    url          = StringField(unique=True)
    imageURL     = StringField()
