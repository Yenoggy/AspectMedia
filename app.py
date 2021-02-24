from flask import Flask, render_template
from articles import articles

app = Flask(__name__)


@app.route('/')
def master():
    return render_template('index.html', title="Аспект", articles=articles)

@app.route('/test')
def test():
    return render_template('test.html', title="NIGGA", articles=articles)


if __name__ == '__main__':
    app.run()
