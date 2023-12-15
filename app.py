from flask import Flask, render_template, get_flashed_messages, request, redirect, url_for, flash
import sqlite3

app = Flask(__name__)
app.secret_key = 'your_random_and_secure_key'

@app.route('/')
def index():
    # Retrieve posts from the database and display them on the index page
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts').fetchall() 
    close_db_connection(conn)
    messages = get_flashed_messages()  # Retrieve flashed messages (e.g., success or error messages)
    return render_template('index.html', posts=posts, messages=messages)

def get_db_connection():
    # Establish a connection to the SQLite database
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row  # Use Row as the row factory to access columns by name
    return conn

def close_db_connection(conn):
    # Close the database connection
    conn.close()

initialized = False  # Flag to track whether initialization has occurred

@app.before_request
def before_request():
    # Initialize the database before the first request
    global initialized
    if not initialized:
        init_db()
        initialized = True
        print("Executing before the first request.")

def init_db():
    # Create the 'posts' table if it does not exist
    conn = get_db_connection()
    conn.execute('CREATE TABLE IF NOT EXISTS posts (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT NOT NULL, content TEXT NOT NULL)')
    conn.close()        

@app.route('/<int:post_id>')
def get_post(post_id):
    # Retrieve a specific post based on its ID and display it
    conn = get_db_connection()
    post = conn.execute('SELECT * FROM posts WHERE id = ?', (post_id,)).fetchone()
    conn.close()
    return render_template('post.html', post=post)

@app.route('/new', methods=['GET', 'POST'])
def new_post():
    # Handle the creation of a new post (GET: display the form, POST: process the form submission)
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        conn = get_db_connection()
        try:
            # Insert a new post into the 'posts' table
            conn.execute('INSERT INTO posts (title, content) VALUES (?, ?)', (title, content))
            conn.commit()
            flash('Post added successfully!', 'success')  # Add a success message
        except Exception as e:
            print(f"Error inserting into the database: {e}")
            conn.rollback()
            flash('Error adding the post. Please try again.', 'error')  # Add an error message
        finally:
            close_db_connection(conn)

        return redirect(url_for('index'))

    return render_template('add_post.html')

@app.route('/verify_database')
def verify_database():
    # Example route to print all data from the 'posts' table in the console
    conn = sqlite3.connect('database.db') 
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM posts')
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    conn.close()

    return 'Data from the database printed in the console.'

if __name__ == '__main__':
    # Run the Flask application
    app.run()
