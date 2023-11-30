from flask import Flask

from vsearch import search_letters

app = Flask(__name__)

@app.route('/')
def hello() -> str:
    return "Hello world from Flask."

@app.route('/search4')
def do_search() -> str:
    return search_letters('marc kooij')

app.run()
