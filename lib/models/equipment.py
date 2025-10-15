from db_setup import get_connection

class Equipment:
    def __init__(self, name, type, Mission, id = None):
        self._name = name
        self._type = type
        self._mission = Mission
        self.id = id

    @property
    def name(self):
        if isinstance(self._name, str) and len(self._name) > 0:
            return self._name
        else:
            raise ValueError("Equipment name must be a non-empty string.")

    @property
    def type(self):
        if isinstance(self._type, str) and len(self._type) > 0:
            return self._type
        else:
            raise ValueError("Equipment type must be a non-empty string.")

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
            return cls(name=row[1], type=row[2], Mission=row[3], id=row[0])
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