from db_setup import get_connection

class Equipment:
    def __init__(self, name, type, Mission, id = None):
        self._name = name
        self._type = type
        self._mission = Mission
        self.id = id