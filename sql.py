import sqlite3

# Connect to SQLite (Creates a new database file if it doesn't exist)
connection = sqlite3.connect("database.db")
cursor = connection.cursor()

# Create the STUDENT table if it doesn't already exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS STUDENT (
    NAME VARCHAR(25),
    CLASS VARCHAR(25),
    SECTION VARCHAR(25),
    MARKS INT
);
""")

# Insert student records (Fixed: Using executemany)
cursor.executemany("""
INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS) VALUES (?, ?, ?, ?)
""", [
    ("Rishi", "CSAI", "AI2", 100),
    ("Tushar", "CSAIML", "AIML4", 100),
    ("Lalit", "CSAIML", "AIML4", 86),
    ("Gautam", "IT", "D", 50),
    ("Harsh", "IT", "D", 35),
    ("Yash", "AIML", "A", 35)
])

# Create the FACULTY table if it doesn't already exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS FACULTY (
    NAME VARCHAR(25),
    DEPARTMENT VARCHAR(25),
    EXPERIENCE INT
);
""")

# Insert faculty records (Fixed: Using executemany)
cursor.executemany("""
INSERT INTO FACULTY (NAME, DEPARTMENT, EXPERIENCE) VALUES (?, ?, ?)
""", [
    ("Prem Sagar", "CDC", 15),
    ("Amit", "CDC", 10),
    ("Prof. Gupta", "AI & ML", 8),
    ("Prof. Sen", "Cybersecurity", 12)
])

# Commit changes and close connection
connection.commit()
connection.close()