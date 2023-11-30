from flask import Flask, render_template
from vsearch import search_letters

app = Flask(__name__)

@app.route('/')
def hello() -> str:
    return "Hello world from Flask."

@app.route('/search4', methods='POST')
def do_search() -> str:
    return str(search_letters('marc kooij'))

@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html', the_title="Welcom to search4letters on the web!")

app.run()
