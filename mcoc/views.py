from flask import Blueprint, flash, redirect, render_template, request, session, url_for
from datetime import datetime

bp = Blueprint('view', __name__, url_prefix='/')

@bp.route("", methods=('GET','POST'))
def home_page():
    day_name = datetime.today().strftime("&A")
    return render_template("home.html", day = day_name)


@bp.route("movies")
def movies_page():
    return render_template("movies.html")
