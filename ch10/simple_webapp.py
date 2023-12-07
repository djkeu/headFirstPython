from flask import Flask, session

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

@app.route('/login')
def do_login() -> str:
    session['logged_in'] = True
    return "U bent ingelogd hoor."

@app.route('/logout')
def do_logout() -> str:
    session.pop('logged_in')
    return 'U bent niet langer ingelogd.'

@app.route('/status')
def check_status() -> str:
    if 'logged_in' in session:
        return "U bent momenteel ingelogd."
    
    return "U bent helemaal niet ingelogd."

app.secret_key = 'allesmag'


if __name__ == '__main__':
    app.run(debug=True)
