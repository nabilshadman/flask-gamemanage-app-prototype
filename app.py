from flask import Flask, render_template, url_for, request, session, redirect, flash
import requests


app = Flask(__name__)
app.secret_key = "gamesearchengine1234"


@app.route("/")
def main():
    raw_data = requests.get("http://www.omdbapi.com/?apikey=d2b6a667&s=resident-evil")
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


@app.route("/collection_list")
def collection_list():
    collection_list = session.get("collection")
    if bool(collection_list) == False:
        flash("Your Collection is empty. Add any game to it!")
        return redirect(url_for("main"))
    else:
        return render_template("collection.html", collection_list=collection_list)


@app.route("/add_to_collection/<title>")
def add_to_collection(title):
    collection_list = {}
    if "collection" in session:
        collection_list = session.get("collection")
    else:
        session["collection"] = {}
    collection_list[title] = title
    session["collection"] = collection_list
    return redirect(url_for("main"))


@app.route("/remove_from_collection/<title>")
def remove_from_collection(title):
    collection_list = session.get("collection")
    collection_list.pop(title, None)
    session["collection"] = collection_list
    return redirect(url_for("collection_list"))


if __name__ == "__main__":
    app.run(debug=True)
