import html  # Prevent undefined variable error in annotations

from flask import Flask, render_template, request, session
from vsearch import search_letters

from DBcm import UseDatabase
from checker import check_logged_in

app = Flask(__name__)

app.config['dbconfig'] = {'host': '127.0.0.1',
                          'user': 'vsearch',
                          'password': 'vsearchpasswd',
                          'database': 'vsearchlogDB', }


@app.route('/login')
def do_login() -> str:
    session['logged_in'] = True
    return 'U bent ingelogd hoor.'


@app.route('/logout')
def do_logout() -> str:
    session.pop('logged_in')
    return 'U bent niet meer ingelogd.'


def log_request(req, res: str) -> None:
    """Log details of the web request and the results."""
    raise Exception("Something awful just happened.")

    with UseDatabase(app.config['dbconfig']) as cursor:
        _sql = """insert into log
            (phrase, letters, ip, browser_string, results)
            values(%s, %s, %s, %s, %s)"""
        cursor.execute(_sql, (req.form['phrase'],
                              req.form['letters'],
                              req.remote_addr,
                              req.user_agent.string,
                              res, ))


@app.route('/search4', methods=['POST'])
def do_search() -> 'html':
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = "Here are you results:"
    results = str(search_letters(phrase, letters))
    try:
        log_request(request, results)
    except Exception as err:
        print("Inloggen mislukt met deze foutmelding:", str(err))
    return render_template('results.html',
                           the_phrase=phrase,
                           the_letters=letters,
                           the_title=title,
                           the_results=results,)


@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template(
        'entry.html',
        the_title="Welcome to search4letters on the web!"
        )


@app.route('/viewlog')
@check_logged_in
def view_the_log() -> 'html':
    """Display the contenst of a log file as HTML table."""
    with UseDatabase(app.config['dbconfig']) as cursor:
        _sql = """select phrase, letters, ip, browser_string, results from log"""
        cursor.execute(_sql)
        contents = cursor.fetchall()
        titles = ('Phrase', 'Letters', 'Remote_addr', 'User_agent', 'Results')

        return render_template('viewlog.html',
                               the_title='View Log',
                               the_row_titles=titles,
                               the_data=contents,)


app.secret_key = 'allesmag'

if __name__ == '__main__':
    app.run(debug=True)
