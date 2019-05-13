from peewee import *
from Services.Auth.DB.PostgresqlController import BaseModel


class Session(BaseModel):
    session = CharField(unique=True, index=True)
    token_id = IntegerField()
    user_id = IntegerField()
