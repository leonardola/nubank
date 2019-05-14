from peewee import *
from Entity import db

class Category(Model):

    id = IntegerField()
    name = CharField()

    class Meta:
        database = db
