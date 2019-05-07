from Services.Auth.DB.Models.Session import Session
from Services.Auth.DB.Models.Token import Token
from Services.Auth.DB.Models.User import User
from Services.Auth.DB.PostgresqlController import db

db.connect()
db.create_tables([User, Token, Session])
