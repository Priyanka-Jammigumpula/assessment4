from flask import Flask, jsonify
import pyodbc
import os

app = Flask(__name__)

@app.route('/employees/<int:dept_id>')
def get_employees(dept_id):
    conn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=' + os.environ['DB_SERVER'] + ';'
        'DATABASE=' + os.environ['DB_NAME'] + ';'
        'UID=' + os.environ['DB_USER'] + ';'
        'PWD=' + os.environ['DB_PASSWORD']
    )
    try:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Employees WHERE DepartmentID = ?', (dept_id,))
        columns = [column[0] for column in cursor.description]
        employees = [dict(zip(columns, row)) for row in cursor.fetchall()]
        return jsonify(employees)
    finally:
        conn.close()

if __name__ == '__main__':
    app.run(debug=True)
