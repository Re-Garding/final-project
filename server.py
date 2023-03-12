"""Server for app."""
from random import choice
from flask import Flask, render_template, request, flash, session, redirect
from model import connect_to_db, db
import crud

from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined
app.jinja_env.auto_reload = True


@app.route("/")
def homepage():
    """View homepage."""
    return render_template("homepage.html")

@app.route("/dashboard/<user_id>")
def dashboard(user_id):
    """get user by id."""
    users = crud.get_user_by_id(user_id)
    return render_template("dashboard.html", users=users)

if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True,use_reloader=True,
    use_debugger=True )

