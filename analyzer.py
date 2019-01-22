import nltk
import tweepy
from textblob import TextBlob
from plotly import tools
import plotly.plotly as py
import plotly.graph_objs as go
import plotly

api_key = "PkbtrP3kPjHf49HXDpD4i2A3x"
api_secret = "HZwErxPBpMOqUMXre4hQdv4ArQqSQ21SDW2jzGDl4tzQuJyqoD"
access_token = "1069492233806798855-jUZ12rIRcqMbNJ0kyoSsL8M6tdTBt0"
access_token_secret = "FEpRC2LgSMsPZj6Hznkta6TWIuBmJe6w3JLJYM9nkhIn3"

def get_tweets(screen_name):
    tweets = []

    auth = tweepy.OAuthHandler(api_key,api_secret)
    auth.set_access_token(access_token,access_token_secret)
    api = tweepy.API(auth)

    last_200_tweets = api.user_timeline(screen_name=screen_name,count=200)
    tweets.extend(last_200_tweets)
    tweets = [tweet.text for tweet in tweets]

    return tweets

def sentiment_analysis_polarity(text):
    analysis = TextBlob(text)
    return analysis.sentiment.polarity

def sentiment_analysis_subjectivity(text):
    analysis = TextBlob(text)
    return analysis.sentiment.subjectivity

def subplot(lst1, lst2):
    data1 = go.Bar(
        x = list(range(200)),
        y = lst1
        # name = 'Polarity'
    )

    data2 = go.Bar(
        x = list(range(200)),
        y = lst2
        # name = 'Subjectivity'
    )

    fig = tools.make_subplots(rows=2, cols=1)

    fig.append_trace(data1, 1, 1)
    fig.append_trace(data2, 2, 1)

    return plotly.offline.plot(fig, output_type="div", show_link=False, link_text=False)
    