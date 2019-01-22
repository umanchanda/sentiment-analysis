from flask import Flask, redirect, render_template, request, url_for
import analyzer

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search")
def search():

    screen_name = request.args.get("screen_name", "").lstrip("@")
    if not screen_name:
        return redirect(url_for("index"))

    polarities = []
    subjectivities = []
    
    for tweet in analyzer.get_tweets(screen_name):
        polarities.append(analyzer.sentiment_analysis_polarity(tweet))
        subjectivities.append(analyzer.sentiment_analysis_subjectivity(tweet))
    
    bar = analyzer.subplot(polarities, subjectivities)

    return render_template("search.html", bar=bar, screen_name=screen_name)