from controllers.controller import Controller, request_mapping

@request_mapping("/a")
class UserController(Controller):
    def __init__(self):
        super().__init__()
    
    @Controller.get_mapping("/")
    def get(self):
        return {"cu": "pinto"}

uc = UserController()