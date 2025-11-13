from controllers.controller import Controller
from services.handler import Handler
import inspect

routes: dict[str, Controller] = {}


def get_methods(uri: str, method: str):
        controller = routes[uri].__class__

        methods = []
        for name, func in inspect.getmembers(controller, predicate=inspect.isfunction):
            if getattr(func, f"_is_{method}", False):
                methods.append((name, func))
        return methods

class Router:
    def get(self, handler: Handler):
        server_path = handler.path
        parse_path = handler.parse_path(server_path)

        gets = get_methods(parse_path["path"], 'GET')

        for name, func in gets:
             func()
