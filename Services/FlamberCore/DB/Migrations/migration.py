from Services.FlamberCore.DB.Models.Session import Session
from Services.FlamberCore.DB.Models.Token import Token
from Services.FlamberCore.DB.Models.User import User
from Services.FlamberCore.DB.Controllers.PostgresqlController import db

db.connect()
db.create_tables([User, Token, Session])
