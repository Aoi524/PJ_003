from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///todo.db')
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Model definition
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    completed = db.Column(db.Boolean, default=False)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    DEBUG = os.getenv('DEBUG', 'FALSE')
    app.run(host='0.0.0.0', debug=DEBUG)