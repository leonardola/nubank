from peewee import *

db = MySQLDatabase('nubank', user='root', password='root',
                   host='10.254.254.254')

db.connect()