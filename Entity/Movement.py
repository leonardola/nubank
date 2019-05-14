from peewee import *
from Entity import db

class Movement(Model):
    STATUS_HIDE = "HIDE"

    id = IntegerField()
    original_name = CharField()
    edited_name = CharField()
    date = DateField()
    value = DecimalField()
    status = CharField()
    type = CharField()
    hash = CharField()

    class Meta:
        database = db
