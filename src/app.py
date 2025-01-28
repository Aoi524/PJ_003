from flask import Flask, render_template, request, redirect, url_for
from dotenv import load_dotenv
import mysql.connector
import os
import time
import mysql.connector
from mysql.connector import Error

load_dotenv()

app = Flask(__name__)

DB_CONFIG = {
    'host': os.getenv('DB_HOST'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'database': os.getenv('DB_NAME')
}

def create_blogs_table():
    con = mysql.connector.connect(**DB_CONFIG)
    cursor = con.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS blogs (
            title VARCHAR(255),
            body TEXT,
            post_date DATE
        )
    """)
    con.commit()
    cursor.close()
    con.close()

def wait_for_mysql_connection(config, retries=10, delay=5):
    for attempt in range(retries):
        try:
            con = mysql.connector.connect(**config)
            con.close()
            print("MySQLに接続成功")
            return
        except Error as e:
            print(f"MySQLに接続失敗: {e}")
            if attempt < retries - 1:
                time.sleep(delay)
    raise Exception("MySQLへの接続に失敗しました。リトライ回数を超えました。")

wait_for_mysql_connection(DB_CONFIG)
create_blogs_table()

@app.route('/')
def index():
    con = mysql.connector.connect(**DB_CONFIG)
    cursor = con.cursor(dictionary=True)
    cursor.execute('SELECT * FROM blogs')
    blogs = cursor.fetchall()
    cursor.close()
    con.close()

    return render_template('index.html', blogs=blogs)

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/register', methods=['POST'])
def register():
    title = request.form['title']
    body = request.form['body']
    post_date = request.form['post_date']

    con = mysql.connector.connect(**DB_CONFIG)
    cursor = con.cursor()
    cursor.execute('INSERT INTO blogs (title, body, post_date) VALUES (%s, %s, %s)', (title, body, post_date))
    con.commit()
    cursor.close()
    con.close()

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)