from flask import Flask, jsonify
from flask_mysqldb import MySQL

app = Flask(__name__)

# Configure the MySQL connection
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'ace'

mysql = MySQL(app)

@app.route('/employees', methods=['GET'])
def get_employees():
    cur = mysql.connection.cursor()
    cur.execute("SELECT id, name, position, salary FROM employees")
    rows = cur.fetchall()

    # Convert the result to a list of dictionaries
    employees = []
    for row in rows:
        employee = {
            'id': row[0],
            'name': row[1],
            'position': row[2],
            'salary': row[3]
        }
        employees.append(employee)

    return jsonify(employees)

if __name__ == '__main__':
    app.run(debug=True)
