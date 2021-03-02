from flask import Flask, render_template
from articles import articles

app = Flask(__name__)


@app.route('/')
def master():
    return render_template('index.html', title="Аспект", articles=articles)

@app.route('/articles/<int:article_id>')
def get_article(article_id):
    return render_template('article.html',
                           articles=articles[article_id - 1],
                           title=articles[article_id - 1]['title'])

if __name__ == '__main__':
    app.run()
