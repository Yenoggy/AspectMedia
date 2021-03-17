from flask import Flask, render_template
from articles import articles
import sqlite3

app = Flask(__name__)


@app.route('/')
def master():
    con = sqlite3.connect('data.db')
    cur = con.cursor()
    cur.execute('SELECT articles.id, articles.title, articles.announcement, users.name FROM articles INNER JOIN users ON articles.user_id = users.id')
    articles = cur.fetchall()
    con.close()
    articles = [{'id': article[0], 'title': article[1], 'body': article[2]} for article in articles]
    return render_template('index.html',
                           title="Аспект",
                           articles=articles)

@app.route('/articles/<int:article_id>')
def get_article(article_id):
    return render_template('article.html',
                           articles=articles[article_id - 1],
                           title=articles[article_id - 1]['title'])

@app.route('/auth')
def auth():
    return render_template('auth.html', title="Вход")


if __name__ == '__main__':
    app.run()
