from flask import Blueprint, flash, redirect, render_template, request, session, url_for
from datetime import datetime
from mcoc.database import add_champion, add_account, remove_champion, remove_account, get_champion

bp = Blueprint('view', __name__, url_prefix='/')

@bp.route("", methods=('GET','POST'))
def home_page():
    day_name = datetime.today().strftime("&A")
    remove_champion(1)
    remove_account("umturock")
    return render_template("home.html", day = day_name)


@bp.route("champs")
def champs_page():
    add_account("umturock","accpsswrd", "accmail", "uncollected", 60)
    add_champion("hulk", 5, 55, 5, 100, "umturock")
    champ = get_champion(1, None, None, None)
    return render_template("champs.html", champ=champ)
