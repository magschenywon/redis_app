from flask import Flask, render_template, redirect, g, request, url_for,current_app
import sqlite3
import redis

DATABASE = redis.Redis('localhost')

app = Flask(__name__)
app.config.from_object(__name__)


@app.route("/")
def show_list():
    db = get_db()
    cur = db.execute('SELECT date, county, state,flips, cases, deaths FROM US_COUNTRIES')
    US_COUNTRIES = cur.fetchall()
    database = [dict(date=row[0], county = row[1], state=row[2], flips =row[3], cases=row[4],deaths = row[5])
              for row in US_COUNTRIES]
    return render_template('index.html', appproject=database)

'''
@app.route("/add", methods=['POST'])
def add_entry():
    db = get_db()
    db.execute('insert into US_COUNTRIES (date, county, state, flips, cases, deaths) values (?,?,?,?,?,?)',
               [request.form['date'], request.form['county'],request.form ['state'],request.form['flips'],request.form['cases'],request.form['deaths']])
    db.commit()
    return redirect(url_for('show_list'))

@app.route("/delete/<item>")
def delete_entry(item):
    db = get_db()
    db.execute("DELETE FROM US_COUNTRIES WHERE date='"+item+"'OR county='"+item+"' OR state='"+item+"' flips = '"+item+"' OR cases='"+item+"' OR deaths ='"+item+"'" )
    db.commit()
    return redirect(url_for('show_list'))
'''

def get_db():
    if 'DATABASE' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db
'''
def get_db():
    """Opens a new database connection if there is none yet for the
    current application context.
    """
    if not hasattr(g, 'CSVDATA_db'):
        g.CSVDATA_db = sqlite3.connect(app.config['DATABASE'])
    return g.sqlite_db
'''

def close_db(e=None):
    db = g.pop('', None)

    if db is not None:
        db.close()
'''
@app.teardown_appcontext
def close_db(error):
    """Closes the database again at the end of the request."""
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()

'''
if __name__ == "_main_":
    app.run("0.0.0.0",port=80)

