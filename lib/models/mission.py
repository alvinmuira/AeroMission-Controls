from db_setup import get_connection

class Mission():
    def __init__(self, name, status, launch_date, id = None):
        self._name = name
        self._status = status
        self._launch_date = launch_date
        self.id = id