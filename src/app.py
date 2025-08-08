from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

# データベースの設定
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://mysql:mysql@booklist-db:3306/BookLists'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# モデルの定義
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    publisher = db.Column(db.String(100), nullable=True)
    published_date = db.Column(db.Date, nullable=False)
    isbn = db.Column(db.String(20), unique=True, nullable=True)
    status = db.Column(db.String(50), nullable=False, default='未読')
    readed_date = db.Column(db.Date, nullable=True)

# 書籍一覧の表示
@app.route('/')
def index():
    books = Book.query.all()
    return render_template('index.html', books=books)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)