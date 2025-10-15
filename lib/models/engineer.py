from db_setup import get_connection

class Engineer:
    def __init__(self, name, specialization, Mission, id = None):
        self._name = name
        self._specialization = specialization
        self._mission = Mission
        self.id = id