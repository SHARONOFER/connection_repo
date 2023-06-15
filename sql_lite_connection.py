
import sqlite3

# Replace 'your_database.db' with the path to your SQLite database file
conn = sqlite3.connect('C:\db_project\pro')

# Create a cursor object to execute SQL queries
cursor = conn.cursor()

# Define the SELECT query
query = "SELECT * FROM test"

# Execute the query
cursor.execute(query)

# Fetch all rows from the result set
rows = cursor.fetchall()

# Process and print the retrieved data
for row in rows:
    print(row)

# Close the cursor and connection
cursor.close()
conn.close()

