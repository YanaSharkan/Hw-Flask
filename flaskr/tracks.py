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
    record = db.execute(
        'SELECT count(*) AS `count`'
        'FROM tracks'
    ).fetchone()
    return render_template('tracks/tracks_count.html', data=record)


@bp.route('/tracks/<genre>')
def get_tracks_by_genre(genre):
    db = get_db()
    record = db.execute(
        'SELECT count(*) AS `count`, genre '
        'FROM tracks WHERE genre = ?',
        (genre,)
    ).fetchone()
    return render_template('tracks/tracks_by_genre.html', data=record)


@bp.route('/tracks-sec')
def get_tracks_with_duration():
    db = get_db()
    records = db.execute(
        'SELECT title, `length` FROM tracks'
    ).fetchall()
    return render_template('tracks/tracks_with_duration.html', data=records)


@bp.route('/tracks-sec/statistics')
def get_tracks_statistics():
    db = get_db()
    record = db.execute(
        'SELECT SUM(length) AS total, AVG(length) AS average '
        'FROM tracks'
    ).fetchone()
    return render_template('tracks/tracks_statistics.html', data=record)
