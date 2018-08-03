#!/usr/bin/python
# -*- coding: utf-8 -*-

from mongoengine import *

connect('sampledatabase', host='10.1.34.63', port=7771)

class Record(Document):
    title        = StringField(max_length=128, required=True)
    description  = StringField()
    url          = StringField(unique=True)
    imageURL     = StringField()
