from db_setup import get_connection

class Engineer:
    def __init__(self, name, specialization, id = None):
        self.name = name
        self.specialization = specialization
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
        return cls(name=row[1], specialization=row[2], id=row[0])
    
    def save(self):
        connection = get_connection()
        cursor = connection.cursor()
        if self.id:
            cursor.execute("""
                UPDATE engineer
                SET name = ?, specialization = ?
                WHERE id = ?;
            """, (self.name, self.specialization, self.id))
        else:
            cursor.execute("""
                INSERT INTO engineer (name, specialization)
                VALUES (?, ?);
            """, (self.name, self.specialization))
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

    @classmethod
    def get_all_engineers(cls):
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM engineer")
        rows = cursor.fetchall()
        connection.close()
        return [cls.new_from_db_row(row) for row in rows]

    def assign_to_mission(self, mission, role):
        from lib.models.engineer_mission import EngineerMission
        if not self.id:
            raise ValueError("Engineer must be saved to the database before assignment.")
        if not mission.id:
            raise ValueError("Mission must be saved to the database before assignment.")
        assignment = EngineerMission(engineer=self, mission=mission, role=role)
        assignment.save()
        return assignment