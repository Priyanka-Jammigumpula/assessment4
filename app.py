from flask import Flask, jsonify
import pymssql

app = Flask(__name__)

@app.route('/employees/<int:dept_id>')
def get_employees(dept_id):
    conn = pymssql.connect(
        server=os.environ['DB_SERVER'],
        user=os.environ['DB_USER'],
        password=os.environ['DB_PASSWORD'],
        database=os.environ['DB_NAME']
    )
    try:
        cursor = conn.cursor(as_dict=True)
        cursor.execute('SELECT * FROM Employees WHERE DepartmentID = %s', (dept_id,))
        employees = cursor.fetchall()
        return jsonify(employees)
    finally:
        conn.close()

if __name__ == '__main__':
    app.run(debug=True)
