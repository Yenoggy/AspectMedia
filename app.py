from typing import List
from flask import Flask, render_template, request, redirect, url_for
from models import db, User, Article
from flask_migrate import Migrate
from forms import ArticleForm
from flask_bootstrap import Bootstrap
from flask_simplemde import SimpleMDE
import json

app = Flask(__name__)
Bootstrap(app)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.sqlite'
app.config['SECRET_KEY'] = 'AWWWWW'
app.config['SIMPLEMDE_JS_IIFE'] = True
app.config['SIMPLEMDE_USE_CDN'] = True
db.app = app
db.init_app(app)
migrate = Migrate(app, db)
SimpleMDE(app)


# Главная
@app.route('/')
def master():
    articles: List[Article] = Article.query.all()
    return render_template('index.html',
                           title="Аспект",
                           articles=articles)


# Вход
@app.route('/auth')
def auth():
    return render_template('auth.html', title="Вход")


# Панель администратора
@app.route('/admin')
def admin_panel():
    data = {'time': 1619017803724, 'blocks': [{'type': 'header', 'data': {'text': 'Главный заголовок текста', 'level': 1}}, {'type': 'paragraph', 'data': {'text': 'А это уже обычный абзац'}}, {'type': 'header', 'data': {'text': 'Не такой крутой заголовок, но тоже ничего', 'level': 3}}, {'type': 'list', 'data': {'style': 'unordered', 'items': ['Эта штука тоже огонь🔥🔥🔥', 'Звать ненумерованный список', 'Удобно что-то тут перечислять']}}, {'type': 'delimiter', 'data': {}}, {'type': 'paragraph', 'data': {'text': 'Здесь можно много чего наворотить. Предлагаю поиграться с редактором самостоятельно😏'}}, {'type': 'image', 'data': {'url': 'static/img/content.png', 'caption': 'Описание картинки', 'withBorder': True, 'withBackground': False, 'stretched': False}}], 'version': '2.20.2'}

    return render_template('admin.html', title='Панель администратора', data=data)


# ==РАБОТА С СТАТЬЯМИ==
# Подробный просмотр статьи
@app.route('/articles/<int:article_id>')
def get_article(article_id):
    articles: Article = Article.query.filter_by(id=article_id).first()
    return render_template('article.html', title=articles.title, articles=articles)


# Написание новой статьи
@app.route('/articles/new/<int:article_id>', methods=('GET', 'POST'))
def new_article(article_id):
    # form = ArticleForm()
    # if request.method == 'POST':
    #     title = form.title.data
    #     body = form.body.data
    #     article = Article(title=title, body=body, user=User.query.first())
    #     db.session.add(article)
    #     db.session.commit()
    #     return redirect(url_for('get_article', article_id=article.id))
    # return render_template('new_article.html', form=form)
    if request.method == 'POST':
        results = json.loads(request.data)
        print(results)
        return json.dumps(results)
    with open('file.json', 'w') as f:
        json.dump(request.form, f)
    return render_template('new_article.html')


# Редактирование статьи
@app.route('/articles/<int:article_id>/edit', methods=["GET", "POST"])
def edit_article(article_id):
    form = ArticleForm()
    article = Article.query.filter_by(id=article_id).first()

    if form.validate_on_submit():
        article.title = form.title.data
        article.body = form.body.data
        db.session.add(article)
        db.session.commit()
        return redirect(url_for("get_article", article_id=article.id))

    form.title.data = article.title
    form.body.data = article.body
    return render_template('edit_article.html', form=form)


# Поиск статей
@app.route('/search')
def search_article():
    q = request.args.get('q', '')
    articles: List[Article] = Article.query.filter(Article.title.like(f'%{q}%') | Article.body.like(f'%{q}%')).all()
    return render_template('index.html',
                           title='Аспект',
                           articles=articles)


# Запуск приложения
if __name__ == '__main__':
    app.run()
