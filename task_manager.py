import sqlite3
import datetime
from typing import List, Tuple

class TaskManager:
    def __init__(self, db_name="tasks.db"):
        self.conn = sqlite3.connect(db_name, check_same_thread=False)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        """Creates the tasks table if it doesn't exist."""
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            description TEXT NOT NULL,
            due_date TIMESTAMP,
            status TEXT DEFAULT 'pending'
        )
        """)
        self.conn.commit()

    def add_task(self, description: str, due_date: datetime.datetime = None) -> int:
        """Adds a new task to the database."""
        sql = "INSERT INTO tasks (description, due_date) VALUES (?, ?)"
        self.cursor.execute(sql, (description, due_date))
        self.conn.commit()
        print(f"DB: Added task '{description}' for {due_date}")
        return self.cursor.lastrowid

    def get_tasks(self, query_date: datetime.date) -> List[Tuple]:
        """Retrieves tasks for a specific date."""
        start_of_day = datetime.datetime.combine(query_date, datetime.time.min)
        end_of_day = datetime.datetime.combine(query_date, datetime.time.max)

        sql = "SELECT description, due_date, status FROM tasks WHERE due_date BETWEEN ? AND ? AND status = 'pending' ORDER BY due_date"
        self.cursor.execute(sql, (start_of_day, end_of_day))
        tasks = self.cursor.fetchall()
        print(f"DB: Found {len(tasks)} tasks for {query_date}")
        return tasks

    def get_all_pending_tasks(self) -> List[Tuple]:
        """Retrieves all tasks that are not marked as 'done'."""
        sql = "SELECT description, due_date, status FROM tasks WHERE status = 'pending' ORDER BY due_date"
        self.cursor.execute(sql)
        tasks = self.cursor.fetchall()
        print(f"DB: Found {len(tasks)} pending tasks in total.")
        return tasks

    def complete_task(self, task_description: str) -> int:
        """
        Marks a task as 'done' using fuzzy matching on the description.
        Returns the number of tasks updated.
        """
        sql = "UPDATE tasks SET status = 'done' WHERE description LIKE ? AND status = 'pending'"
        query_param = f"%{task_description}%"
        self.cursor.execute(sql, (query_param,))
        self.conn.commit()
        updated_rows = self.cursor.rowcount
        print(f"DB: Matched and completed {updated_rows} task(s) for description like '{task_description}'")
        return updated_rows

    def close(self):
        """Closes the database connection."""
        self.conn.close()