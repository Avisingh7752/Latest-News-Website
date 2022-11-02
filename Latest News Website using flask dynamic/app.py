from flask import Flask, render_template, request
import requests
from sqlalchemy import true

app = Flask(__name__)

@app.route("/")
def index():
    url = "https://newsapi.org/v2/top-headlines?country=in&apiKey=a8fa6629509c4d38b03a235675808339"
    r = requests.get(url).json() # to convert API to json file

    cases = {
        'articles' : r['articles']
    }

    return render_template("index.html", case = cases)



if __name__== "__main__":
    app.run(debug=True)