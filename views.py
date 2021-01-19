from server import app

@app.route("/")
def home_page():
    day_name = datetime.today().strftime("&A")
    return render_template("home.html", day = day_name)


@app.route("/movies")
def movies_page():
    return render_template("movies.html")
