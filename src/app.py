from flask import Flask, render_template, request, redirect, url_for
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
    tasks = Task.query.all()
    return render_template('index.html', tasks=tasks)

@app.route('/add_task', methods=['GET','POST'])
def add_task():
    if request.method == 'POST':
        task_content = request.form['content']
        new_task = Task(content=task_content)

        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except:
            db.session.rollback()
            return 'There was an issue adding your task'

    return render_template('add_task.html')

@app.route('/toggle_complete/<int:id>', methods=['POST'])
def toggle_complete(id):
    task = Task.query.get_or_404(id)
    task.completed = not task.completed

    try:
        db.session.commit()
        return redirect('/')
    except:
        db.session.rollback()
        return 'There was an issue updating the task'

@app.route('/delete_task/<int:id>', methods=['POST'])
def delete_task(id):
    task = Task.query.get_or_404(id)

    try:
        db.session.delete(task)
        db.session.commit()
        return redirect('/')
    except:
        db.session.rollback()
        return 'There was an issue deleting the task'

if __name__ == '__main__':
    DEBUG = os.getenv('DEBUG', 'FALSE')
    app.run(host='0.0.0.0', debug=DEBUG)