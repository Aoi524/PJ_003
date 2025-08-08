from flask import Flask, render_template, request, redirect, url_for
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

# 書籍の登録画面の表示
@app.route('/register', methods=['GET'])
def register():
    return render_template('register_book.html')

# 書籍の編集画面の表示
@app.route('/update/<id>', methods=['GET'])
def update(id):
    book = Book.query.filter_by(id=id).first()
    return render_template('register_book.html', book=book)

# 書籍の登録
@app.route('/register', methods=['POST'])
def register_book():
    title = request.form['title']
    author = request.form['author']
    publisher = request.form['publisher']
    published_date = request.form['published_date']
    isbn = request.form['isbn']
    status = request.form['status']
    readed_date = request.form['readed_date'] if request.form['readed_date'] else None

    book = Book(
        title=title,
        author=author,
        publisher=publisher,
        published_date=published_date,
        isbn=isbn,
        status=status,
        readed_date=readed_date
    )
    db.session.add(book)
    db.session.commit()
    return redirect(url_for('index'))

# 書籍の編集
@app.route('/update/<id>', methods=['POST'])
def update_book(id):
    title = request.form['title']
    author = request.form['author']
    publisher = request.form['publisher']
    published_date = request.form['published_date']
    isbn = request.form['isbn']
    status = request.form['status']
    readed_date = request.form['readed_date'] if request.form['readed_date'] else None

    book = Book.query.filter_by(id=id).first()
    book.title = title
    book.author = author
    book.publisher = publisher
    book.published_date = published_date
    book.isbn = isbn
    book.status = status
    book.readed_date = readed_date

    db.session.commit()

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)