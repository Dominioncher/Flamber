import importlib.util
from autobahn.asyncio.component import run, Component
import glob
import os
from Core import Core
from Core.Core import Api


def connect(url: str):

    # Инициализируем соединение с диспатчером
    Core.api = Api(transports=url)

    # Импортим все Api методы
    modules = glob.glob(os.path.abspath("Api")+"/*.py")
    for module in modules:
        name = os.path.basename(module)[:-3]
        spec = importlib.util.spec_from_file_location(name, module)
        foo = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(foo)

    # Стартуем сервак
    run(Core.api)
