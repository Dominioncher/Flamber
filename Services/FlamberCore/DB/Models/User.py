from peewee import *
from Services.FlamberCore.DB.Controllers.PostgresqlController import BaseModel


class User(BaseModel):
    login = CharField(unique=True, index=True)
    password = CharField()
