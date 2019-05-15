from peewee import *
from Entity import db
from Entity.Movement import Movement
from Entity.Category import Category

class Movement_has_Category(Model):

    category = ForeignKeyField(Category)
    movement = ForeignKeyField(Movement)

    class Meta:
        database = db
