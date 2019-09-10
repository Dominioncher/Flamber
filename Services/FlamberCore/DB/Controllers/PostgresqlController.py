from peewee import Model
from playhouse.db_url import connect

db = connect('postgres://cwkqcpzzddirtu:fb55d52bb2ea762ff1b317a8d10e1ee3751e35ae3fc632cfb7230c4e3b59d38c@ec2-54-247-72-30.eu-west-1.compute.amazonaws.com:5432/d855ht7o9huevl')


class BaseModel(Model):
    class Meta:
        database = db
