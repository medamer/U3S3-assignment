# web_app/routes/tweet_routes.py

from flask import Blueprint, jsonify, request, render_template
from web_app.models import Tweet, db, parse_records

tweet_routes = Blueprint("tweet_routes", __name__)

@tweet_routes.route("/tweets.json")
def list_tweets():

    tweet_records = Tweet.query.all()
    print(tweet_records)
    tweets = parse_records(tweet_records)
    return jsonify(tweets)

@tweet_routes.route("/tweets")
def list_tweets_for_humans():
    
    tweet_records = Tweet.query.all()
    print(tweet_records)
    tweets = parse_records(tweet_records)
    return render_template("tweets.html", message="Here's the list of tweets", tweets=tweets)

@tweet_routes.route("/tweets/add")
def add_tweet():
    return render_template("add_tweet.html")

@tweet_routes.route("/tweets/create", methods=["POST"])
def create_tweet():
    print("FORM DATA:", dict(request.form))

    # INSERT INTO tweeta db ...
    add_tweet = Tweet(tweet=request.form["tweet"], tweeter_id=request.form["tweeter_name"])
    db.session.add(add_tweet)
    db.session.commit()

    # to store in the database
    return jsonify({
        "message": "Tweet added successfully!",
        "tweet": dict(request.form)
    })