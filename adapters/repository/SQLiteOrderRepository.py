import sqlite3
from repository import OrderRepository

class SQLiteOrderRepository(OrderRepository):
    def __init__(self, db_path):
        self.conn = sqlite3.connect(db_path)  # Cria o arquivo se não existir [[3]]
        self._create_table()

    def _create_table(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS orders (
                id TEXT PRIMARY KEY,
                customer_name TEXT NOT NULL,
                total_amount REAL NOT NULL,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        self.conn.commit()