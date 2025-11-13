from http import HTTPStatus
from core import router
#from database.database import Database

def request_mapping(uri: str):
    def wrapper(cls):
        cls._uri = uri
        return cls
    return wrapper

class Controller():
    def __init__(self):
        self.uri = self._uri
        if self.uri not in router.routes:
            router.routes[self.uri] = self

    @classmethod
    def get_mapping(self, uri: str):
        def wrapper(func):
            func._is_GET = True
            func._uri = uri
            return func
        return wrapper
    
    def get(self):
        ...
