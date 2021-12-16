"""
GameManage Flask Web Application.
"""


# import relevant libraries and packages
from flask import Flask, render_template, url_for, request, session, redirect, flash
import requests


# initialize flask app
app = Flask(__name__)
app.secret_key = "gamesearchengine1234"


@app.route("/")
def main():
    """
    This function is the application's main route. The function 
    renders the homepage template from various locations in the 
    website.

    :return: home.html
    :rtype: HTML
    """
    raw_data = requests.get("https://api.boardgameatlas.com/api/search?name=board&client_id=JLBr5npPhV")
    games = raw_data.json()
    return render_template("home.html", games=games)


@app.route("/<name>")
def games_by_name(name):
    """
    This function is a variation from the main() function. It 
    renders the homepage template with a different set of games displayed
    based on name keyword parameter from the Board Game Atlas (BGA) API. 
    This function is useful to test the homepage with various set 
    of featured games.

    :param name: name keyword to search for in BGA API
    :type name: string

    :return: home.html
    :rtype: HTML
    """
    raw_data = requests.get("https://api.boardgameatlas.com/api/search?name="+name+"&client_id=JLBr5npPhV")
    games = raw_data.json()
    return render_template("home.html", games=games)


@app.route("/single_game/<id>")
def single_game(id):
    """
    This function renders a template to display specific information 
    about a particular game. The function receives a game 'id' parameter, 
    which is then used to query for the specific game from the BGA API.

    :param id: game id to search for in BGA API
    :type id: int

    :return: single_game.html
    :rtype: HTML
    """
    raw_data = requests.get("https://api.boardgameatlas.com/api/search?ids="+id+"&client_id=JLBr5npPhV")
    game = raw_data.json()
    return render_template("single_game.html", game=game)


@app.route("/search")
def search_form():
    """
    This function renders the search template to display search engine 
    results.

    :return: search.html
    :rtype: HTML
    """
    return render_template("search.html")


@app.route("/search_by_name", methods=["POST"])
def search_by_name():
    """
    This function is the logic for the game search engine. The
    funtion receives either name, or both name and year from
    the user from the search page via a POST request. Then, the
    function searches for games with the input from the BGA API, 
    and renders the search page with the returned results from
    the API.

    :return: search.html
    :rtype: HTML
    """
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
    """
    This function renders the collection list of the user. If
    the collection is empty, a flash message is displayed suggesting
    user to add games to her collection.

    :return: collection.html
    :rtype: HTML
    """
    collection_list = session.get("collection")
    if bool(collection_list) == False:
        flash("Your Collection is empty. Add any game to it!")
        return render_template("collection.html", collection_list=collection_list)
    else:
        return render_template("collection.html", collection_list=collection_list)


@app.route("/add_to_collection/<id>")
def add_to_collection(id):
    """
    This function adds a particular game to the user's collection.
    It takes a game id as a parameter, and then queries for the
    particular game from the BGA API, and then stores the id and 
    the game's name in a dictionary.

    :param id: game id to search for in BGA API
    :type id: int

    :return: main()
    :rtype: function
    """
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
    """
    This function removes a particular game from the user's collection.
    It takes game id key as a parameter and then removes the (key,value)
    pair from the collection_list dictionary.

    :param id: game id key
    :type id: int

    :return: collection_list()
    :rtype: function
    """
    collection_list = session.get("collection")
    collection_list.pop(id, None)
    session["collection"] = collection_list
    return redirect(url_for("collection_list"))


if __name__ == "__main__":
    app.run(debug=True)
