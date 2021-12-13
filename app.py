from flask import Flask, render_template, url_for, request, session, redirect, flash
import requests


app = Flask(__name__)
app.secret_key = "gamesearchengine1234"


@app.route("/")
def main():
    raw_data = requests.get("https://api.boardgameatlas.com/api/search?name=board&client_id=JLBr5npPhV")
    games = raw_data.json()
    return render_template("home.html", games=games)


@app.route("/<name>")
def games_by_name(name):
    raw_data = requests.get("https://api.boardgameatlas.com/api/search?name="+name+"&client_id=JLBr5npPhV")
    games = raw_data.json()
    return render_template("home.html", games=games)


@app.route("/single_game/<id>")
def single_game(id):
    raw_data = requests.get("https://api.boardgameatlas.com/api/search?ids="+id+"&client_id=JLBr5npPhV")
    game = raw_data.json()
    return render_template("single_game.html", game=game)


@app.route("/search")
def search_form():
    return render_template("search.html")


@app.route("/search_by_name", methods=["POST"])
def search_by_name():
    name = request.form["name"]
    year = request.form["year"]
    if year != "":
        raw_data = requests.get(
            "https://api.boardgameatlas.com/api/search?name="+name
            +"&year_published="+year
            +"&client_id=JLBr5npPhV")
    else:
        raw_data = requests.get(
            "https://api.boardgameatlas.com/api/search?name="+name
            +"&client_id=JLBr5npPhV")
    games = raw_data.json()
    return render_template("search.html", games=games)


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
