import pyodbc

server = "<SQL_SERVER>.database.windows.net"
database = "salesdb"
username = "sqladmin"
password = "Password@12345"

connection_string = f"""
DRIVER={{ODBC Driver 18 for SQL Server}};
SERVER={server};
DATABASE={database};
UID={username};
PWD={password};
Encrypt=yes;
TrustServerCertificate=no;
Connection Timeout=30;
"""

conn = pyodbc.connect(connection_string)

cursor = conn.cursor()

cursor.execute("SELECT * FROM Customers")

rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()
