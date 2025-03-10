# AI-Powered SQL Query Generator

![AI-Powered SQL Query Generator](./Screenshot%202025-03-10%20215856.png)

## Introduction
The **AI-Powered SQL Query Generator** is a smart tool that allows users to generate and execute SQL queries using voice and text inputs. This application integrates AI to convert natural language queries into SQL, making database interactions seamless for users without deep SQL knowledge.

## Features
- 🎤 **Voice & Text Support**: Users can input queries using speech or text.
- 💬 **LLM to SQL Converter**: Transforms natural language queries into SQL commands.
- 🧠 **AI-Powered Query Generation**: AI-driven query creation for ease of use.
- 📊 **Live SQL Execution**: Run SQL queries instantly on the selected database.
- 🌍 **Multi-Lingual Support**: Supports over 100 languages for global accessibility.

## Database Setup
This project uses an SQLite database (`database.db`). The schema consists of two tables: `STUDENT` and `FACULTY`.

### STUDENT Table
Stores student details:
- `NAME` (VARCHAR) - Student's name
- `CLASS` (VARCHAR) - Class name
- `SECTION` (VARCHAR) - Section
- `MARKS` (INT) - Marks obtained

#### Sample Entries:
| NAME   | CLASS  | SECTION | MARKS |
|--------|--------|---------|-------|
| Rishi  | CSAI   | AI2     | 100   |
| Tushar | CSAIML | AIML4   | 100   |
| Lalit  | CSAIML | AIML4   | 86    |
| Gautam | IT     | D       | 50    |
| Harsh  | IT     | D       | 35    |
| Yash   | AIML   | A       | 35    |

### FACULTY Table
Stores faculty information:
- `NAME` (VARCHAR) - Faculty's name
- `DEPARTMENT` (VARCHAR) - Department name
- `EXPERIENCE` (INT) - Years of experience

#### Sample Entries:
| NAME                | DEPARTMENT     | EXPERIENCE |
|---------------------|---------------|------------|
| Dr. Premsagar Sharma | CDC           | 15         |
| Amit Pandey        | CDC           | 10         |
| Prof. Gupta       | AI & ML       | 8          |
| Prof. Sen        | Cybersecurity | 12         |

## Installation & Usage

### Prerequisites
- Python 3.x
- SQLite3
- Streamlit (`pip install streamlit`)

### Running the Application
1. Clone this repository:
   ```sh
   git clone https://github.com/your-repo/sql-query-generator.git
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

## Contributing
Feel free to contribute by submitting issues or pull requests!

## License
This project is licensed under the MIT License.

---
**Author**: Rishi Varshney
