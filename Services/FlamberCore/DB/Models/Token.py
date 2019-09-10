from peewee import *
from Services.FlamberCore.DB.Controllers.PostgresqlController import BaseModel


class Token(BaseModel):
    token = CharField(unique=True, index=True)
    user_id = IntegerField()
