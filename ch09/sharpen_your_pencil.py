@app.route('/viewlog')
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
