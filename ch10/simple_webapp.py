from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello() -> str:
    return 'Hallo, ik ben een simpele webapp.'

@app.route('/page1')
def page1() -> str:
    return 'Dit is bladzijde 1'

@app.route('/page2')
def page2() -> str:
    return 'Pagina twee'

@app.route('/page3')
def page3() -> str:
    return 'Derde set'

if __name__ == '__main__':
    app.run(debug=True)
