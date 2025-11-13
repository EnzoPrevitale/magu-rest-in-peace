from core import server
from controllers.controller import Controller, request_mapping

@request_mapping("/a")
class TestController(Controller):
    def __init__(self):
        super().__init__()

    @Controller.get_mapping("/a")
    def get():
        print("cu")

@request_mapping("/b")
class AController(Controller):
    def __init__(self):
        super().__init__()

    @Controller.get_mapping("/b")
    def get():
        print("buceta")

cont = TestController()
cont2 = AController()

if __name__ == '__main__':
    server.run_server()
