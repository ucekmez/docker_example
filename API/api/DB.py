#!/usr/bin/python
# -*- coding: utf-8 -*-

from mongoengine import *

connect('sampledatabase', host='database', port=7777)

class Record(Document):
    title        = StringField(max_length=128, required=True)
    description  = StringField()
    url          = StringField(unique=True)
    imageURL     = StringField()
