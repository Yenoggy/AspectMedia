from typing import List
from flask import Flask, render_template
from models import db, User, Article
from flask_migrate import Migrate


app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///D:/Study/ITMO Project/test.sqlite'
db.app = app
db.init_app(app)
migrate = Migrate(app, db)


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
