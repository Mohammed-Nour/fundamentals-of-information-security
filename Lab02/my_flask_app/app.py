from flask import Flask, render_template, request, redirect, url_for
from flask_basicauth import BasicAuth
import mysql.connector
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

app = Flask(__name__)


limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["200 per day", "50 per hour"]
)

# Initialize Flask-BasicAuth
basic_auth = BasicAuth(app)

# Define a list of allowed users and their passwords
app.config['BASIC_AUTH_USERNAME'] = 'user1'
app.config['BASIC_AUTH_PASSWORD'] = 'password1'

# Configure MySQL database connection
app.config['MYSQL_HOST'] = 'localhost'  # Replace with your MySQL host
app.config['MYSQL_USER'] = 'myflaskappuser'  # Replace with your MySQL username
app.config['MYSQL_PASSWORD'] = 'gda hglkd;i'  # Replace with your MySQL password
app.config['MYSQL_DB'] = 'myflaskappdb'  # Replace with your MySQL database name

# Create a MySQL connection
mysql_conn = mysql.connector.connect(
    host=app.config['MYSQL_HOST'],
    user=app.config['MYSQL_USER'],
    password=app.config['MYSQL_PASSWORD'],
    database=app.config['MYSQL_DB']
)

# Define a cursor to execute SQL queries
cursor = mysql_conn.cursor()

# Define a table for storing entries
create_table_query = """
CREATE TABLE IF NOT EXISTS entries (
    id INT AUTO_INCREMENT PRIMARY KEY,
    entry_text TEXT
);
"""

cursor.execute(create_table_query)
mysql_conn.commit()

# example no limit route
@app.route('/')
@limiter.exempt
def home():
    return render_template('home.html')

# example 5 per minute route 
# Define the data_entry route to handle form submission
@app.route('/data_entry', methods=['GET', 'POST'])
@limiter.limit("5 per minute")
@basic_auth.required
def data_entry():
    if request.method == 'POST':
        entry_text = request.form['entry_text']
        # Insert the entry into the database
        insert_query = "INSERT INTO entries (entry_text) VALUES (%s)"
        cursor.execute(insert_query, (entry_text,))
        mysql_conn.commit()

    # Retrieve all entries from the database
    select_query = "SELECT * FROM entries"
    cursor.execute(select_query)
    entries = cursor.fetchall()

    return render_template('data_entry.html', entries=entries)

if __name__ == '__main__':
    app.run()
