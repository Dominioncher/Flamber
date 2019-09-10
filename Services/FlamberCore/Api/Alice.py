from Core.Core import api
from Services.FlamberCore.Scripts.DialogFlow import DialogFlow as df


@api.register('api/v1/user_question')
def user_question(text: str) -> str:
    try:
        answer = df.message(text)
    except:
        answer = 'Я вас не поняла. Вы можете повторить свой запрос?'

    return answer
