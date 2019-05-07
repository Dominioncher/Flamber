from peewee import *
from Services.Auth.DB.PostgresqlController import BaseModel


class Token(BaseModel):
    token = CharField(unique=True, index=True)
    user_id = IntegerField()
