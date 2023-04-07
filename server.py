"""Server for app."""

import random
from random import choice
from flask import Flask, render_template, request, flash, session, redirect,jsonify
from model import connect_to_db, db
import crud

from jinja2 import StrictUndefined
app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined
app.jinja_env.auto_reload = True

@app.route('/')
def homepage():
    """View homepage."""
    user_id = session.get('user_id')
    user = crud.get_user_by_id(user_id)
    user_name = user.first_name
    return render_template("homepage.html", user_name=user_name)

@app.route("/users", methods=["POST"])
def register_user():
    """Create a new user."""
    email = request.form.get("email")
    password = request.form.get("password")
    age_input = request.form.get("age_input")
    first_name = request.form.get("first_name")
    last_name = request.form.get("last_name")

    user = crud.get_user_by_email(email)
    if user:
        flash("Cannot create an account with that email. Try again.")
    else:
        user = crud.create_user(first_name, last_name , email,age_input, password)
        db.session.add(user)
        db.session.commit()
        flash("Account created! Please log in.")
        session['user_email'] = user.email
        session['user_id'] = user.user_id

    return redirect("/")

@app.route("/login", methods=["POST"])
def process_login():
    """User Login."""

    email = request.form.get("email")
    password = request.form.get("password")

    user = crud.get_user_by_email(email)
    if not user or user.password != password:
        flash("The email or password you entered was incorrect.")
    else:
        session["user_email"] = user.email
        session['user_id'] = user.user_id
        flash(f"Welcome back, {user.first_name}!")

    return redirect("/dashboard")        
@app.route('/dashboard_data')
def word_quiz():

    words = crud.get_dictionarywords()
    random_words = random.choice(words)
    quiz = crud.get_quizquestions()
    random_quiz = random.choice(quiz) 

    data= {
        'daily_quiz' :{'Question':random_quiz.question,
                       'A': random_quiz.answer_choice_1,
                       'B': random_quiz.answer_choice_2,
                       'C': random_quiz.answer_choice_3,
                       'D': random_quiz.answer_choice_4,
                       'correct_reasoning': random_quiz.correct_answer_reasoning,
                       'tryagain': random_quiz.incorrect_answer_feedback
                       },   

        'daily_words' :{'words':random_words.dict_key_id,
                       'word': random_words.definition
                       }   
        
    }
    return (jsonify(data))

@app.route('/dashboard')
def dashboard_route():
    """notepage."""
    user_id = session.get('user_id')
    user = crud.get_user_by_id(user_id)
    user_name = user.first_name
    return render_template ('dashboard.html', user_name = user_name)
   
@app.route("/notepage")
def notes():
    """notepage."""
    user_id = session.get('user_id', "")
    print("notepage")
    print(user_id)
    if (user_id):
        note_by_user = crud.get_note(session['user_id'])
    else:
        note_by_user = ""
    return render_template("notes.html", note_by_user=note_by_user)

@app.route("/notepage_save",methods=["POST"])
def notes_save():
    """notepage."""
    user_id = session.get('user_id', "")
    note = request.form.get("note")
    create_note = crud.create_notepage(user_id, note)
    return redirect("/nextsteps")

@app.route("/nextsteps")
def next_steps():
    """notepage."""
    user_id = session.get('user_id')
    user = crud.get_user_by_id(user_id)
    user_name = user.first_name
    return render_template("thankyou.html", user_name =user_name)

if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True,use_reloader=True,
    use_debugger=True )

