from flask import Flask, render_template, url_for, request, session, redirect, flash
import requests


app = Flask(__name__)
app.secret_key = "gamesearchengine1234"


@app.route("/")
def main():
    raw_data = requests.get("https://api.boardgameatlas.com/api/search?name=Catan&client_id=JLBr5npPhV")
    movies = raw_data.json()
    return render_template("home.html", movies=movies)


@app.route("/<title>")
def movies_by_title(title):
    raw_data = requests.get("http://www.omdbapi.com/?apikey=d2b6a667&s="+title)
    movies = raw_data.json()
    return render_template("home.html", movies=movies)


@app.route("/single_movie/<id>")
def single_movie(id):
    raw_data = requests.get("https://api.boardgameatlas.com/api/search?ids="+id+"&client_id=JLBr5npPhV")
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
        raw_data = requests.get("http://www.omdbapi.com/?apikey=d2b6a667&s="+title+"&y="+year)
    else:
        raw_data = requests.get("http://www.omdbapi.com/?apikey=d2b6a667&s="+title)
    movies = raw_data.json()
    return render_template("search.html", movies=movies)


@app.route("/collection_list")
def collection_list():
    collection_list = session.get("collection")
    if bool(collection_list) == False:
        flash("Your Collection is empty. Add any game to it!")
        return render_template("collection.html", collection_list=collection_list)
    else:
        return render_template("collection.html", collection_list=collection_list)


@app.route("/add_to_collection/<id>")
def add_to_collection(id):
    collection_list = {}
    if "collection" in session:
        collection_list = session.get("collection")
    else:
        session["collection"] = {}
    game = requests.get(
        "https://api.boardgameatlas.com/api/search?ids="+
        id+"&client_id=JLBr5npPhV").json()
    collection_list[id] = game['games'][0]['name']
    session["collection"] = collection_list
    flash("The game has been added to your Collection!")
    return redirect(url_for("main"))


@app.route("/remove_from_collection/<id>")
def remove_from_collection(id):
    collection_list = session.get("collection")
    collection_list.pop(id, None)
    session["collection"] = collection_list
    return redirect(url_for("collection_list"))


if __name__ == "__main__":
    app.run(debug=True)
