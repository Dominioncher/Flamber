import secrets
from autobahn.wamp import CallDetails, ApplicationError
from Core.Core import api


users = dict()
users['Artyom'] = 'Artyom30000'
tokens = dict()
session_user = dict()


@api.register('api/v1/register')
def register(username: str, password: str) -> bool:
    if username in users:
        raise ApplicationError('error', 'Username already used')
    users[username] = password
    return True


@api.register('api/v1/authentication')
def authentication(username: str, password: str) -> str:
    if username not in users:
        raise ApplicationError(ApplicationError.AUTHENTICATION_FAILED)

    if users[username] != password:
        raise ApplicationError(ApplicationError.AUTHENTICATION_FAILED)

    token = secrets.token_hex()
    tokens[token] = username

    return token


@api.register('api/v1/authorization')
def authorization(token: str, details: CallDetails) -> bool:
    if token not in tokens:
        raise ApplicationError(ApplicationError.AUTHORIZATION_FAILED)

    session_user[details.caller] = token
    return True


@api.register('api/v1/logout')
def authorization(details: CallDetails) -> bool:
    if details.caller not in session_user:
        raise ApplicationError(ApplicationError.AUTHORIZATION_FAILED)

    token = session_user[details.caller]
    del tokens[token]
    del session_user[details.caller]
    return True
