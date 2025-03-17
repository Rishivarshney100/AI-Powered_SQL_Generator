# AI-Powered SQL Query Generator

![Screenshot 2025-03-10 215856](https://github.com/user-attachments/assets/9c445baa-4bc9-4143-9c3a-eaae3dd14523)


## Introduction
The **AI-Powered SQL Query Generator** is a smart tool that allows users to generate and execute SQL queries using voice and text inputs. This application integrates AI to convert natural language queries into SQL, making database interactions seamless for users without deep SQL knowledge.

## 🚀 Project Overview

This project is a **voice-enabled SQL query app** built using:

- **SQLite3** for database management
- **Streamlit** for a user-friendly UI
- **SpeechRecognition** for converting speech to text
- **Google Gemini AI** to generate SQL queries from user input
- **Deep Translator** for language translation support

With this system, users can:

- **Create tables**, **insert records**, and **query data** using natural language.
- Use **speech recognition** to generate SQL queries via voice commands.
- **List, display, and manipulate tables dynamically** with AI assistance.

## 📂 Project Structure

```plaintext
.
├── app.py                # Main Streamlit app with AI-powered SQL query execution
├── database.db           # SQLite database file (created dynamically)
├── requirements.txt      # Required Python dependencies
├── .env                  # Environment file storing API keys
└── README.md             # Project documentation (this file)
```

## Features
- 🎤 **Voice & Text Support**: Users can input queries using speech or text.
- 💬 **LLM to SQL Converter**: Transforms natural language queries into SQL commands.
- 🧠 **AI-Powered Query Generation**: AI-driven query creation for ease of use.
- 📊 **Live SQL Execution**: Run SQL queries instantly on the selected database.
- 🌍 **Multi-Lingual Support**: Supports over 100 languages for global accessibility.

## Database Setup
This project uses an SQLite database (`database.db`).

## Installation & Usage

### Prerequisites
- Python 3.x
- SQLite3
- Streamlit (`pip install streamlit`)

### Running the Application
1. Clone this repository:
   ```sh
   git clone https://github.com/AI-Powered_SQL_Generator/sql-query-generator.git
   ```
2. Navigate to the project directory:
   ```sh
   cd sql-query-generator
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Run the Streamlit application:
   ```sh
   streamlit run app.py
   ```

## How It Works
1. Select the database file (`database.db`).
2. Use the **Show Table Count** button to verify available tables.
3. Input queries using text or speech.
4. Click **Generate SQL Query** to convert natural language to SQL.
5. Execute the query with the **Execute Query** button.

## 🛠 Troubleshooting

### ❌ "Table does not exist"

🔹 Ensure that tables are created before querying them:

```sql
SELECT name FROM sqlite_master WHERE type='table';
```

If the table is missing, manually create it or check the database file.

### ❌ "Multiple SQL statements error"

🔹 SQLite does not support multiple statements in `execute()`. To fix this:

```python
cursor.executescript('''
CREATE TABLE IF NOT EXISTS STUDENT (...);
CREATE TABLE IF NOT EXISTS FACULTY (...);
''')
```

## Contributing
Feel free to contribute by submitting issues or pull requests!
