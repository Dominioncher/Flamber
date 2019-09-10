from peewee import *
from Services.FlamberCore.DB.Controllers.PostgresqlController import BaseModel


class Session(BaseModel):
    session = CharField(unique=True, index=True)
    token_id = IntegerField()
    user_id = IntegerField()
