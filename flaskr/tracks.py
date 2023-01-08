from flask import (
    Blueprint, render_template
)


from flaskr.db import get_db

bp = Blueprint('tracks', __name__)


@bp.route('/names')
def get_names():
    db = get_db()
    names_count = db.execute(
       'SELECT count(distinct artist) AS `count`'
       'FROM tracks'
    ).fetchone()
    return render_template('tracks/names.html', data=names_count)


@bp.route('/tracks')
def get_number_of_records():
    db = get_db()
    records = db.execute(
        'SELECT count(*) AS `count`'
        'FROM tracks'
    ).fetchone()
    return render_template('tracks/tracks_count.html', data=records)


