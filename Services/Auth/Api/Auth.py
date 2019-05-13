import secrets
from autobahn.wamp import CallDetails, ApplicationError
from Core.Core import api
from Services.Auth.DB.Models.Session import Session
from Services.Auth.DB.Models.Token import Token
from Services.Auth.DB.Models.User import User


@api.register('api/v1/register')
def register(login: str, password: str) -> bool:
    if User.get_or_none(User.login == login):
        raise ApplicationError('error', 'Username already used')

    User.create(login=login, password=password)
    return True


@api.register('api/v1/authentication')
def authentication(login: str, password: str) -> str:
    user = User.get(User.login == login)
    if not user or user.password != password:
        raise ApplicationError(ApplicationError.AUTHENTICATION_FAILED)

    token = secrets.token_hex()
    Token.create(token=token, user_id=user.id)
    return token


@api.register('api/v1/authorization')
def authorization(token: str, details: CallDetails) -> bool:
    tok = Token.get(Token.token == token)
    session = Session.get_or_none(Session.session == details.caller)
    if session:
        session.token_id = tok.id
        session.user_id = tok.user_id
        session.save()
    else:
        Session.create(session=details.caller, token_id=tok.id, user_id=tok.user_id)
    return True


@api.register('api/v1/logout')
def logout(details: CallDetails) -> bool:
    curr_session = Session.get(Session.session == details.caller)
    Session.delete().where(Session.token_id == curr_session.token_id).execute()
    Token.delete().where(Token.id == curr_session.token_id).execute()
    return True


@api.register('api/v1/get_user_sessions')
def get_user_sessions(user_id: int) -> []:
    sessions = Session.select().where(Session.user_id == user_id)
    ids = []
    for session in sessions:
        ids.append(session.session)
    return ids
