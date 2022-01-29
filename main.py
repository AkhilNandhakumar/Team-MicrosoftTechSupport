from __init__ import app
from flask import render_template, request
from flask import request, redirect
import requests

from beach_features import sortBestBeaches, allBeachCriteriaMustMatch, anyBeachCriteriaCanMatch
from crud.app_crud import app_crud
from crud.app_crud_api import app_crud_api
app.register_blueprint(app_crud)
app.register_blueprint(app_crud_api)

# app.routes

@app.route('/')
def index():
    return render_template("/index.html")

@app.route('/reviews/')
def reviews():
    return render_template("/assignments/reviews.html")

# ---------------- BEACHES --------------------

@app.route('/solana-beach/')
def SolanaBeach():
    import requests
    url = "https://tides.p.rapidapi.com/tides"

    querystring = {"longitude":"-117.272469","latitude":"32.989262","interval":"60","duration":"1440"}

    headers = {
        'x-rapidapi-host': "tides.p.rapidapi.com",
        'x-rapidapi-key': "af654d789amshce4b35d071f3bd2p1c0cc8jsn8db3aa6a8acc"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    tides = response.json()

    return render_template("/assignments/Beaches/SolanaBeach.html", tides=tides)

@app.route('/del-mar-beach/')
def DelMarBeach():
    import requests
    url = "https://tides.p.rapidapi.com/tides"

    querystring = {"longitude":"-117.872269","latitude":"33.603588","interval":"60","duration":"1440"}

    headers = {
        'x-rapidapi-host': "tides.p.rapidapi.com",
        'x-rapidapi-key': "af654d789amshce4b35d071f3bd2p1c0cc8jsn8db3aa6a8acc"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    tides = response.json()

    return render_template("/assignments/Beaches/DelMarBeach.html", tides=tides)

@app.route('/blacks-beach/')
def BlacksBeach():
    import requests
    url = "https://tides.p.rapidapi.com/tides"

    querystring = {"longitude":"-117.253716","latitude":"32.898354","interval":"60","duration":"1440"}

    headers = {
        'x-rapidapi-host': "tides.p.rapidapi.com",
        'x-rapidapi-key': "af654d789amshce4b35d071f3bd2p1c0cc8jsn8db3aa6a8acc"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    tides = response.json()

    return render_template("/assignments/Beaches/BlacksBeach.html", tides=tides)

@app.route('/pacific-beach/')
def PacificBeach():
    import requests
    url = "https://tides.p.rapidapi.com/tides"

    querystring = {"longitude":"-117.236748","latitude":"32.782021","interval":"60","duration":"1440"}

    headers = {
        'x-rapidapi-host': "tides.p.rapidapi.com",
        'x-rapidapi-key': "af654d789amshce4b35d071f3bd2p1c0cc8jsn8db3aa6a8acc"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    tides = response.json()

    return render_template("/assignments/Beaches/PacificBeach.html", tides=tides)

@app.route('/beachlocation3/')
def BeachLocation3():
    return render_template("/assignments/Beaches/BeachLocation3.html")

def selectBestBeach(form):
    return "DelMar is the best beach for you"

@app.route('/favoritebeach1/', methods=["GET", "POST"])
def FavoriteBeachSurvey():
    feedback = "Beach Not Identified"
    n = 0
    beach_features = []
    requests = list(request.form.items())
    sortMustMatch = False

# GO through the form we got from Survey.html POST and see what sort was selected (Any, All)
    if request.method == "POST":
        if "SORT" in request.form:
            sortMustMatch = True
        else:
            sortMustMatch = False

    if request.method == "POST":
        for field in request.form:
            if field != "SORT":
                beach_features.append (field)
                n = n + 1
        print (beach_features)
        if (sortMustMatch == True):
            beaches = sortBestBeaches(allBeachCriteriaMustMatch, beach_features)
        else:
            beaches = sortBestBeaches(anyBeachCriteriaCanMatch, beach_features)

        print (beaches)
        if (n == 0):
            feedback = "\nunknown! Pick something!"
        else:
            feedback = beaches

    return render_template("/assignments/Survey.html", beach = feedback)

@app.route('/yash/')
def yash():
    url = "https://yourf1.p.rapidapi.com/drivers"

    headers = {
        'x-rapidapi-host': "yourf1.p.rapidapi.com",
        'x-rapidapi-key': "80e73128e0mshda8c95123266391p176951jsnbc06ff234f92"
    }

    response = requests.request("GET", url, headers=headers)
    data = response.json()
    return render_template("/assignments/AboutUs/yash.html", data=data)


@app.route('/akhil/')
def akhil():

    url = "https://sportscore1.p.rapidapi.com/tennis-rankings/wta"
    querystring = {"page":"1"}
    headers = {
        'x-rapidapi-host': "sportscore1.p.rapidapi.com",
        'x-rapidapi-key': "af654d789amshce4b35d071f3bd2p1c0cc8jsn8db3aa6a8acc"
    }

    responseTwo = requests.request("GET", url, headers=headers, params=querystring)
    WTAdata = responseTwo.json()

    url = "https://sportscore1.p.rapidapi.com/tennis-rankings/atp"
    querystring = {"page":"1"}
    headers = {
        'x-rapidapi-host': "sportscore1.p.rapidapi.com",
        'x-rapidapi-key': "af654d789amshce4b35d071f3bd2p1c0cc8jsn8db3aa6a8acc"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    data = response.json()

    return render_template("/assignments/AboutUs/akhil.html", data=data, WTAdata=WTAdata)


@app.route('/valen/')
def valen():
    import requests

    url = "https://nfl-team-stats.p.rapidapi.com/v1/nfl-stats/teams/win-stats/2021"

    headers = {
        'x-rapidapi-host': "nfl-team-stats.p.rapidapi.com",
        'x-rapidapi-key': "dabdc2fe99mshcfa1ae8827f4f16p1f550djsn5f1b6441c796"
    }
    response = requests.request("GET", url, headers=headers)
    chargers=response.json()


    print(response.text)
    return render_template("/assignments/AboutUs/valen.html", chargers=chargers)


@app.route('/avinh/', methods=['GET', 'POST'])
def avinh():
    if request.form:
        pokemon = request.form.get("input")
        PokemonAPI = requests.get("https://pokeapi.co/api/v2/pokemon/" + pokemon)
        PokemonImage = (PokemonAPI.json()["sprites"]["front_default"])
        return render_template("/assignments/AboutUs/avinh.html", PokemonImage=PokemonImage)
    return render_template("/assignments/AboutUs/avinh.html")


@app.route('/jay/')
def jay():
    import requests

    url = "https://nhl-stats-and-live-data.p.rapidapi.com/standings"

    querystring = {"date":"2018-01-09","season":"20032004"}

    headers = {
        'x-rapidapi-host': "nhl-stats-and-live-data.p.rapidapi.com",
        'x-rapidapi-key': "39c4bf8c2emsh30b02ab6dc01dd9p13f427jsn690a650cf2ec"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    var = response.json()
    return render_template("/assignments/AboutUs/jay.html", var=var)


# run page lol
if __name__ == "__main__":
    app.run(debug=True)
