import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_name = 'db.sqlite3'
DB_file = ROOT_DIR / DB_name
TABLE_NAME = 'customers'

connection = sqlite3.connect(DB_file)
cursor =  connection.cursor()

cursor.execute(
    f'CREATE TABLE IF NOT EXISTS {TABLE_NAME}'
    '('
     'id INTEGER PRIMARY KEY AUTOINCREMENT  '   
    ')'
)



cursor.close()
connection.close()