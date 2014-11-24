from flask import Flask
from flask_flatpages import FlatPages
from flask import render_template

DEBUG = True
FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_EXTENSION = ".md"

app = Flask(__name__)
app.config.from_object(__name__)
pages = FlatPages(app)


@app.route('/')
@app.route('/<name>')
def index(name=None):
    return render_template('index.html', pages=pages)


@app.route('/blog/<path:path>/')
def page(path):
    page = pages.get_or_404(path)
    return render_template('page.html', page=page)

if __name__ == "__main__":
    app.run(port=8000)
