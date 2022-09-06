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



def get_db():
    if 'DATABASE' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db


def close_db(e=None):
    db = g.pop('', None)

    if db is not None:
        db.close()

if __name__ == "_main_":
    app.run("0.0.0.0",port=80)

