from typing import List
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///D:/Study/ITMO Project/test.sqlite'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    name = db.Column(db.String(80), unique=False, nullable=False)
    surname = db.Column(db.String(80), unique=False, nullable=False)
    password = db.Column(db.String(120), unique=False, nullable=False)
    admin = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.nickname

class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(1000), unique=False, nullable=False)
    body = db.Column(db.Text(), unique=False, nullable=True)
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('articles', lazy=True))

    def __repr__(self):
        return f'Title: {self.title}'

@app.route('/')
def master():
    articles: List[Article] = Article.query.all()
    return render_template('index.html',
                           title="Аспект",
                           articles=articles)

@app.route('/articles/<int:article_id>')
def get_article(article_id):
    articles: Article = Article.query.filter_by(id=article_id).first()
    return render_template('article.html', title=articles.title, articles=articles)

@app.route('/auth')
def auth():
    return render_template('auth.html', title="Вход")


if __name__ == '__main__':
    app.run()
