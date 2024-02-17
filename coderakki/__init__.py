from flask import Flask


def main_app():
    app = Flask(__name__)

    from coderakki.portfolio.routes import portfolio
    app.register_blueprint(portfolio)

    return app
