import secrets
from autobahn.wamp import CallDetails, ApplicationError
from Core.Core import api
from Services.Auth.DB import RedisController as redis
from Services.Auth.DB import MongoController as mongo

@api.register('api/v1/register')
def register(login: str, password: str) -> bool:
    if mongo.db["Users"].find_one({"login": login}):
        raise ApplicationError('error', 'Username already used')

    mongo.db["Users"].insert({'login': login, 'password': password})
    return True


@api.register('api/v1/authentication')
def authentication(login: str, password: str) -> str:
    user = mongo.db["Users"].find_one({"login": login, "password": password})
    if not user:
        raise ApplicationError(ApplicationError.AUTHENTICATION_FAILED)

    token = secrets.token_hex()
    mongo.db["Tokens"].insert({"token": token, "user_id": user['_id']})
    return token


@api.register('api/v1/authorization')
def authorization(token: str, details: CallDetails) -> bool:
    token = mongo.db["Tokens"].find_one({'token': token})
    if not token:
        raise ApplicationError(ApplicationError.AUTHORIZATION_FAILED)

    redis.db.hset('Sessions_tokens', details.caller, str(token['_id']))
    return True


@api.register('api/v1/logout')
def logout(details: CallDetails) -> bool:
    token = redis.db.hget('Sessions_tokens', details.caller)
    if not token:
        raise ApplicationError(ApplicationError.AUTHORIZATION_FAILED)

    sessions = redis.db.hscan('Sessions_tokens', match=token)
    redis.db.hdel('Sessions_tokens', sessions)
    mongo.db["Tokens"].remove(token)
    return True
