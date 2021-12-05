from flask import Flask, render_template, url_for, request, session, redirect, flash
import requests


app = Flask(__name__)
app.secret_key = "moviesearchengine1234"


@app.route("/")
def main():
    raw_data = requests.get("http://www.omdbapi.com/?apikey=d2b6a667&s=batman")
    movies = raw_data.json()
    return render_template("home.html", movies=movies)


@app.route("/<title>")
def movies_by_title(title):
    raw_data = requests.get("http://www.omdbapi.com/?apikey=d2b6a667&s="+title)
    movies = raw_data.json()
    return render_template("home.html", movies=movies)


@app.route("/single_movie/<title>")
def single_movie(title):
    raw_data = requests.get("http://www.omdbapi.com/?apikey=d2b6a667&t="+title)
    movie = raw_data.json()
    return render_template("single_movie.html", movie=movie)


@app.route("/search")
def search_form():
    return render_template("search.html")


@app.route("/search_by_title", methods=["POST"])
def search_by_title():
    title = request.form["title"]
    year = request.form["year"]
    if year != "":
        raw_data = requests.get("http://www.omdbapi.com/?apikey=d2b6a667&t="+title+"&y="+year)
    else:
        raw_data = requests.get("http://www.omdbapi.com/?apikey=d2b6a667&t="+title)
    movie = raw_data.json()
    return render_template("search.html", movie=movie)


@app.route("/favorites_list")
def favorites_list():
    favorites_list = session.get("favorites")
    if bool(favorites_list) == False:
        flash("Your Collection is empty. Add any game to it!")
        return redirect(url_for("main"))
    else:
        return render_template("favorites.html", favorites_list=favorites_list)


@app.route("/add_to_favorites/<title>")
def add_to_favorites(title):
    favorites_list = {}
    if "favorites" in session:
        favorites_list = session.get("favorites")
    else:
        session["favorites"] = {}
    favorites_list[title] = title
    session["favorites"] = favorites_list
    return redirect(url_for("main"))


@app.route("/remove_from_favorites/<title>")
def remove_from_favorites(title):
    favorites_list = session.get("favorites")
    favorites_list.pop(title, None)
    session["favorites"] = favorites_list
    return redirect(url_for("favorites_list"))


if __name__ == "__main__":
    app.run(debug=True)
