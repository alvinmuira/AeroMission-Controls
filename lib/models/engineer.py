from db_setup import get_connection

class Engineer:
    def __init__(self, name, specialization, Mission, id = None):
        self.name = name
        self.specialization = specialization
        self.mission = Mission
        self.id = id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and len(value.strip()) > 0:
            self._name = value
        else:
            raise ValueError("Name must be a non-empty string.")

    @property
    def specialization(self):
        return self._specialization

    @specialization.setter
    def specialization(self, value):
        if isinstance(value, str) and len(value.strip()) > 0:
            self._specialization = value
        else:
            raise ValueError("Specialization must be a non-empty string.")

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
        cursor.execute("SELECT * FROM engineer WHERE id = ?", (id,))
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
            return cls(name=row[1], specialization=row[2], Mission=mission, id=row[0])
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