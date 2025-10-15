from db_setup import get_connection

class Engineer:
    def __init__(self, name, specialization, Mission, id = None):
        self._name = name
        self._specialization = specialization
        self._mission = Mission
        self.id = id

    @property
    def name(self):
        if isinstance(self._name, str) and len(self._name) > 0:
            return self._name
        else:
            raise ValueError("Engineer name must be a non-empty string.")

    @property
    def specialization(self):
        if isinstance(self._specialization, str) and len(self._specialization) > 0:
            return self._specialization
        else:
            raise ValueError("Specialization must be a non-empty string.")

    @classmethod
    def find_by_id(cls, id):
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM engineer WHERE id = ?", (id,))
        row = cursor.fetchone()
        connection.close()
        return cls.new_from_db_row(row)

    @classmethod
    def new_from_db_row(cls, row):
        if row:
            return cls(name=row[1], specialization=row[2], Mission=row[3], id=row[0])
        return None
    
    def save(self):
        connection = get_connection()
        cursor = connection.cursor()
        if self.id:
            cursor.execute("""
                UPDATE engineer
                SET name = ?, specialization = ?, mission_id = ?
                WHERE id = ?;
            """, (self.name, self.specialization, self._mission.id if self._mission else None, self.id))
        else:
            cursor.execute("""
                INSERT INTO engineer (name, specialization, mission_id)
                VALUES (?, ?, ?);
            """, (self.name, self.specialization, self._mission.id if self._mission else None))
            self.id = cursor.lastrowid
        connection.commit()
        connection.close()

    def delete(self):
        if self.id:
            connection = get_connection()
            cursor = connection.cursor()
            cursor.execute("DELETE FROM engineer WHERE id = ?", (self.id,))
            connection.commit()
            connection.close()
            self.id = None
        else:
            raise ValueError("Cannot delete an unsaved Engineer instance.")