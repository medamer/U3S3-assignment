# web_app/routes/home_routes.py

from flask import Blueprint

home_routes = Blueprint("home_routes", __name__)

@home_routes.route("/")
def index():
    return "Welcome to My Tweets Web App"

@home_routes.route("/about")
def about():
    return "About me:", "\n", "My name is Mohamed Edamer, I am Data scientist in Lambda school."