class BaseModel:

    def as_json(self) -> dict:
        return self.__dict__
    