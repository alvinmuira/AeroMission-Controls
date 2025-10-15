from db_setup import get_connection

class Equipment:
    def __init__(self, name, type, Mission, id = None):
        self._name = name
        self._type = type
        self._mission = Mission
        self.id = id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and len(value.strip()) > 0:
            self._name = value
        else:
            raise ValueError("Equipment name must be a non-empty string.")

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        if isinstance(value, str) and len(value.strip()) > 0:
            self._type = value
        else:
            raise ValueError("Equipment type must be a non-empty string.")

    @property
    def mission(self):
        return self._mission

    @mission.setter
    def mission(self, value):
        from lib.models.mission import Mission
        if isinstance(value, Mission):
            self._mission = value
        else:
            raise ValueError("mission must be an instance of Mission class.")

    @classmethod
    def find_by_id(cls, id):
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM equipment WHERE id = ?", (id,))
        row = cursor.fetchone()
        connection.close()
        return cls.new_from_db_row(row)

    @classmethod
    def new_from_db_row(cls, row):
        if row:
            from lib.models.mission import Mission
            mission = Mission.find_by_id(row[3])
            if not mission:
                raise ValueError("Mission with given ID does not exist.")
            return cls(name=row[1], type=row[2], Mission=mission, id=row[0])
        return None

    def save(self):
        connection = get_connection()
        cursor = connection.cursor()
        if self.id:
            cursor.execute("""
                UPDATE equipment
                SET name = ?, type = ?, mission_id = ?
                WHERE id = ?;
            """, (self.name, self.type, self._mission.id if self._mission else None, self.id))
        else:
            cursor.execute("""
                INSERT INTO equipment (name, type, mission_id)
                VALUES (?, ?, ?);
            """, (self.name, self.type, self._mission.id if self._mission else None))
            self.id = cursor.lastrowid
        connection.commit()
        connection.close()

    def delete(self):
        if self.id:
            connection = get_connection()
            cursor = connection.cursor()
            cursor.execute("DELETE FROM equipment WHERE id = ?", (self.id,))
            connection.commit()
            connection.close()
            self.id = None  # Clear the id after deletion
        else:
            raise ValueError("Cannot delete an unsaved Equipment instance.")

    @classmethod
    def get_all_equipment(cls):
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM equipment")
        rows = cursor.fetchall()
        connection.close()
        return [cls.new_from_db_row(row) for row in rows if row]