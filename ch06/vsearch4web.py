from flask import Flask, render_template, request
import html

from vsearch import search_letters

app = Flask(__name__)

def log_request(req, res: str) -> None:
    filename = 'vsearch.log'
    with open(filename, 'a') as log:
        print(req, res, file=log)

@app.route('/search4', methods=['POST'])
def do_search() -> 'html':
    phrase = request.form['phrase']
    letters = request.form['letters']
    title= "Here are you results:"
    results = str(search_letters(phrase, letters))
    log_request(request, results)

    return render_template('results.html', 
                           the_phrase=phrase, 
                           the_letters=letters, 
                           the_title=title,
                           the_results=results,)

@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html', the_title="Welcom to search4letters on the web!")


if __name__ == '__main__':
    app.run(debug=True)
