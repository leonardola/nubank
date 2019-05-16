from peewee import *
import yaml

with open('config.yml', 'r') as f:
    doc = yaml.load(f)

db = MySQLDatabase(doc['db']['name'], user=doc['db']['user'], password=doc['db']['password'],
                   host=doc['db']['host'])

db.connect()
