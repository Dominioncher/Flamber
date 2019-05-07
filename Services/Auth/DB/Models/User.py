from peewee import *
from Services.Auth.DB.PostgresqlController import BaseModel


class User(BaseModel):
    login = CharField(unique=True, index=True)
    password = CharField()
