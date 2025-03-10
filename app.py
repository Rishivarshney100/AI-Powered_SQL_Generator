import os
import sqlite3
import streamlit as st
import speech_recognition as sr
from dotenv import load_dotenv
import google.generativeai as genai
from deep_translator import GoogleTranslator

# Load environment variables
load_dotenv()

# Configure Google Gemini AI
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Initialize Translator
translator = GoogleTranslator(source='auto', target='en')

# Function to translate input to English
def translate_to_english(text):
    try:
        return translator.translate(text)
    except Exception as e:
        st.error(f"Translation Error: {e}")
        return text  # Return original text if translation fails

# Function to get response from Gemini AI
def get_gemini_response(question, prompt):
    try:
        model = genai.GenerativeModel('gemini-2.0-flash')
        response = model.generate_content([prompt[0], question])
        sql_query = response.text.strip() if response.text else "No response received."

        # ✅ Fix: Handle "show tables" correctly
        if "show tables" in question.lower() or "list tables" in question.lower():
            sql_query = "SELECT name FROM sqlite_master WHERE type='table';"

        # ✅ Fix: Handle "show a specific table" correctly
        elif "show table" in question.lower() or "display table" in question.lower():
            words = question.split()
            if len(words) >= 3:  # Ensure there is a table name in the question
                table_name = words[-1]  # Assume the last word is the table name
                sql_query = f"SELECT * FROM {table_name};"
            else:
                sql_query = "Error: No table name provided."

        return sql_query
    except Exception as e:
        st.error(f"AI Model Error: {e}")
        return "Error in generating SQL query."

def table_exists(table_name, db):
    """Check if a table exists in the database."""
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?", (table_name,))
    table = cur.fetchone()
    conn.close()
    return table is not None

# Function to execute SQL queries
def read_sql_query(sql, db):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    
    sql = sql.strip()  # Remove leading/trailing spaces

    try:
        # ✅ Allow multiple SQL statements execution
        cur.executescript(sql)
        conn.commit()
        
        # If SELECT query is present, fetch results
        if "select" in sql.lower():
            cur.execute(sql.split(";")[-2])  # Run the last SELECT statement
            rows = cur.fetchall()
            return rows if rows else "✅ Query executed, but no data found."
        else:
            return "✅ All queries executed successfully."
    
    except sqlite3.OperationalError as e:
        return f"SQL Error: {str(e)}"
    
    finally:
        conn.close()

# Function to convert long speech to text
def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("Listening... Speak as long as you want!")
        
        recognizer.adjust_for_ambient_noise(source, duration=1)  # Adjust for background noise
        
        try:
            audio = recognizer.listen(source, timeout=None, phrase_time_limit=None)  
            text = recognizer.recognize_google(audio)
            st.success(f"Recognized Speech: {text}")
            return text
        
        except sr.UnknownValueError:
            st.error("Could not understand the speech. Please try again.")
            return None
        except sr.RequestError:
            st.error("Speech recognition service is unavailable.")
            return None

# SQL Prompt for Gemini AI
prompt = [
    """
    You are an expert in converting English questions to SQL queries!
    The SQL database consists of multiple tables like STUDENT, COLLEGE, FACULTY with their respective columns.
    You can create more tables, delete any table, perform JOIN operations as well as use aggregate functions, if the user say so.

    Example 1 - How many entries of records are present in student table?
    The SQL command will be: SELECT COUNT(*) FROM STUDENT;

    Example 2 - Tell me all the students studying in Data Science class?
    The SQL command will be: SELECT * FROM STUDENT WHERE CLASS="Data Science";

    Example 3 - Create a new table named TEACHERS with columns NAME and SUBJECT.
    The SQL command will be: CREATE TABLE IF NOT EXISTS TEACHERS (NAME TEXT, SUBJECT TEXT);
    
    Example 3 - Write an SQL query to fetch the names of employees, their departments, the projects they are assigned to, and the total hours they worked on those projects. Also, include employees who are not assigned to any project.
    The SQL command will be: SELECT e.Name AS EmployeeName, d.DepartmentName, p.ProjectName, COALESCE(a.HoursWorked, 0) AS TotalHoursWorked
                        FROM Employees e
                        LEFT JOIN Departments d ON e.DepartmentID = d.DepartmentID
                        LEFT JOIN Assignments a ON e.EmployeeID = a.EmployeeID
                        LEFT JOIN Projects p ON a.ProjectID = p.ProjectID;

    The SQL code should not have at the beginning or end and should not contain the word "sql" in the output.
    """
]

# Streamlit App
st.set_page_config(page_title="Voice-Enabled SQL Query App", layout="wide")

st.sidebar.header("Settings")
db_file = st.sidebar.text_input("Database File", "database.db")

st.title("💬 AI-Powered SQL Query Generator")

col1, col2 = st.columns([1, 1])

with col1:
    if st.button("📊 Show Table Count", use_container_width=True):
        conn = sqlite3.connect(db_file)
        cur = conn.cursor()
        
        cur.execute("SELECT COUNT(*) FROM sqlite_master WHERE type='table';")
        table_count = cur.fetchone()[0]
        
        st.write(f"📂 **Total tables in the database:** {table_count}")

        conn.close()

    if st.button("🎙 Use Speech Input", use_container_width=True):
        spoken_text = speech_to_text()
        if "Error" not in spoken_text:
            st.session_state["speech_input"] = spoken_text
        else:
            st.error(spoken_text)

    question = st.text_input("🔍 Enter your query:", value=st.session_state.get("speech_input", ""))
    if st.button("🧠 Generate SQL Query", use_container_width=True):
        sql_query = get_gemini_response(question, prompt)
        st.session_state["sql_query"] = sql_query  # Store in session state
        st.code(sql_query, language='sql')

    if st.button("📊 Execute Query", use_container_width=True):
        if "sql_query" in st.session_state:
            result = read_sql_query(st.session_state["sql_query"], db_file)
            st.write(result)
        else:
            st.error("⚠️ Please generate a SQL query first!")

with col2:
    st.markdown("**App Features:**")
    st.markdown("- 🎤 Voice & Text Support")
    st.markdown("- 💬 LLM to SQL Converter")
    st.markdown("- 🧠 AI-Powered Query Generation")
    st.markdown("- 📊 Live SQL Execution")
    st.markdown("- 💬 Multi-Lingual support of about 100+ languages")
    