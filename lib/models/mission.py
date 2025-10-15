from db_setup import get_connection

class Mission():
    def __init__(self, name, status, launch_date, id = None):
        self._name = name
        self._status = status
        self._launch_date = launch_date
        self.id = id

    @property
    def name(self):
        if isinstance(self._name, str) and len(self._name) > 0:
            return self._name
        else:
            raise ValueError("Mission name must be a non-empty string.")
        
    @property
    def status(self):
        if self._status in ["Pending", "Ongoing", "Completed", "Aborted"]:
            return self._status
        else:
            raise ValueError("Status must be one of: Pending, Ongoing, Completed, Aborted.")

    @property
    def launch_date(self):
        if isinstance(self._launch_date, str) and len(self._launch_date) > 0:
            return self._launch_date
        else:
            raise ValueError("Launch date must be a non-empty string.")

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
    
