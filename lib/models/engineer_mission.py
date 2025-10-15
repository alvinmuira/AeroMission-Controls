from db_setup import get_connection

class EngineerMission:
    def __init__(self, Engineer, Mission, role, id=None):
        self.engineer = Engineer
        self.mission = Mission
        self.role = role
        self.id = id

    @property
    def engineer(self):
        return self._engineer

    @property
    def mission(self):
        return self._mission

    @property
    def role(self):
        return self._role

    @engineer.setter
    def engineer(self, value):
        from lib.models.engineer import Engineer
        if isinstance(value, Engineer):
            self._engineer = value
        else:
            raise ValueError("engineer must be an instance of Engineer class.")

    @mission.setter
    def mission(self, value):
        from lib.models.mission import Mission
        if isinstance(value, Mission):
            self._mission = value
        else:
            raise ValueError("mission must be an instance of Mission class.")

    @role.setter
    def role(self, value):
        if isinstance(value, str) and len(value.strip()) > 0:
            self._role = value
        else:
            raise ValueError("Role must be a non-empty string.")

    @classmethod
    def find_by_id(cls, id):
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM engineer_mission WHERE id = ?", (id,))
        row = cursor.fetchone()
        connection.close()
        return cls.new_from_db_row(row)

    @classmethod
    def new_from_db_row(cls, row):
        from lib.models.engineer import Engineer
        from lib.models.mission import Mission
        if row:
            engineer = Engineer.find_by_id(row[1])
            mission = Mission.find_by_id(row[2])
            if not engineer:
                raise ValueError("Engineer with given ID does not exist.")
            if not mission:
                raise ValueError("Mission with given ID does not exist.")
            return cls(engineer=engineer, mission=mission, role=row[3], id=row[0])
        return None

    def save(self):
        connection = get_connection()
        cursor = connection.cursor()
        if self.id:
            cursor.execute("""
                UPDATE engineer_mission
                SET engineer_id = ?, mission_id = ?, role = ?
                WHERE id = ?;
            """, (self.engineer.id, self.mission.id, self.role, self.id))
        else:
            cursor.execute("""
                INSERT INTO engineer_mission (engineer_id, mission_id, role)
                VALUES (?, ?, ?);
            """, (self.engineer.id, self.mission.id, self.role))
            self.id = cursor.lastrowid
        connection.commit()
        connection.close()

    def delete(self):
        if not self.id:
            raise ValueError("Cannot delete an engineer-mission assignment that has not been saved to the database.")
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("DELETE FROM engineer_mission WHERE id = ?", (self.id,))
        connection.commit()
        connection.close()
        self.id = None