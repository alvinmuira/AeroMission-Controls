from db_setup import get_connection

class Mission():
    def __init__(self, name, status, launch_date, id = None):
        self.name = name
        self.status = status
        self.launch_date = launch_date
        self.id = id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and len(value.strip()) > 0:
            self._name = value
        else:
            raise ValueError("Mission name must be a non-empty string.")
        
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        types = ["Pending", "Ongoing", "Completed", "Cancelled"]
        if value in types:
            self._status = value.strip()
        else:
            raise ValueError(f"Status must be one of: {', '.join(types)}")

    @property
    def launch_date(self):
        return self._launch_date

    @launch_date.setter
    def launch_date(self, value):
        if not isinstance(value, str) or len(value.strip()) == 0:
            raise ValueError("Launch date must be a non-empty string in 'YYYY-MM-DD' format.")
        try:
            from datetime import datetime
            datetime.strptime(value, "%Y-%m-%d")
            self._launch_date = value
        except ValueError:
            raise ValueError("Launch date must be in 'YYYY-MM-DD' format. eg: '2023-10-15'")
            

    @classmethod
    def find_by_id(cls, id):
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM missions WHERE id = ?", (id,))
        row = cursor.fetchone()
        connection.close()
        return cls.new_from_db_row(row)

    @classmethod
    def new_from_db_row(cls, row):
        if row:
            return cls(name=row[1], status=row[2], launch_date=row[3], id=row[0])
        return None

    def save(self):
        connection = get_connection()
        cursor = connection.cursor()
        if self.id:
            cursor.execute("""
                UPDATE missions
                SET name = ?, status = ?, launch_date = ?
                WHERE id = ?;
            """, (self.name, self.status, self.launch_date, self.id))
        else:
            cursor.execute("""
                INSERT INTO missions (name, status, launch_date)
                VALUES (?, ?, ?);
            """, (self.name, self.status, self.launch_date))
            self.id = cursor.lastrowid
        connection.commit()
        connection.close()

    def delete(self):
        if not self.id:
            raise ValueError("Cannot delete a mission that has not been saved to the database.")
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("DELETE FROM missions WHERE id = ?", (self.id,))
        connection.commit()
        connection.close()
        self.id = None  # Clear the id after deletion
    
    def view_mission_engineers(self):
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("""
            SELECT
                engineer.name,
                engineer.specialization,
                engineer_mission.role
            FROM engineer
            JOIN engineer_mission ON engineer.id = engineer_mission.engineer_id
            WHERE engineer_mission.mission_id = ?
        """, (self.id,))
        results = cursor.fetchall()
        connection.close()
        if results:
            for result in results:
                print(f"The engineer \"{result[0]}\", specialized in \"{result[1]}\", will serve as \"{result[2]}\" in mission \"{self.name}\".")
        else:
            print(f"The \"{self.name}\" mission has no assigned engineers.")

    def view_mission_equipment(self):
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("""
            SELECT
                name,
                type
            FROM equipment
            WHERE mission_id = ?
        """, (self.id,))
        results = cursor.fetchall()
        connection.close()
        if results:
            for result in results:
                print(f"The \"{result[0]}\" equipment of type \"{result[1]}\", will be used in mission \"{self.name}\".")
        else:
            print(f"The \"{self.name}\" mission has no assigned equipment.")

    @classmethod
    def get_missions_with_status(cls, status):
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM missions WHERE status = ?", (status,))
        rows = cursor.fetchall()
        connection.close()
        missions = [cls.new_from_db_row(row) for row in rows]
        return missions

    @classmethod
    def get_all_missions(cls):
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM missions")
        rows = cursor.fetchall()
        connection.close()
        missions = [cls.new_from_db_row(row) for row in rows]
        return missions

    def assign_an_engineer(self, engineer, role):
        from lib.models.engineer_mission import EngineerMission
        if not self.id:
            raise ValueError("Mission must be saved to the database before assignment.")
        if not engineer.id:
            raise ValueError("Engineer must be saved to the database before assignment.")
        assignment = EngineerMission(Engineer=engineer, Mission=self, role=role)
        assignment.save()
        return assignment

    @classmethod
    def find_mission_by_name(cls, name):
        if not isinstance(name, str) or len(name.strip()) == 0:
            raise ValueError("Mission name must be a non-empty string.")
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM missions WHERE name = ?", (name,))
        row = cursor.fetchone()
        connection.close()
        return cls.new_from_db_row(row)

    @classmethod
    def create(cls, name, status, launch_date):
        if not isinstance(name, str) or len(name.strip()) == 0:
            raise ValueError("Mission name must be a non-empty string.")
        if status not in ['Pending', 'Ongoing', 'Completed', 'Cancelled']:
            raise ValueError("Invalid mission status.")
        if not isinstance(launch_date, str) or len(launch_date.strip()) == 0:
            raise ValueError("Launch date must be a non-empty string.")

        mission = cls(name=name, status=status, launch_date=launch_date)
        mission.save()
        return mission
