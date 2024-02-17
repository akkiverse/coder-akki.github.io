from flask import Blueprint, render_template

portfolio = Blueprint("portfolio", __name__)


@portfolio.route("/")
@portfolio.route("/home")
def home():
    return render_template("home.html", title="Home")