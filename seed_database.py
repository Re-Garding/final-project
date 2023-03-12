"""Script to seed database."""

import os
import json
from random import choice, randint
from datetime import datetime

import crud
import model
import server

os.system("dropdb apptest")
os.system("createdb apptest")

model.connect_to_db(server.app)
model.db.create_all()


# Load movie data from JSON file
with open("data/users.json") as f:
    users_data = json.loads(f.read())


# Load movie data from JSON file
with open("data/rewards.json") as f:
    rewards_data = json.loads(f.read())


# Load movie data from JSON file
with open("data/quizquestions.json") as f:
    quizquestions_data = json.loads(f.read())

# Load movie data from JSON file
with open("data/next_steps.json") as f:
    next_steps_data = json.loads(f.read())

# Load movie data from JSON file
with open("data/dictionary.json") as f:
    dictionary_data = json.loads(f.read())

# Load movie data from JSON file
with open("data/books_podcasts.json") as f:
    books_podcasts_data = json.loads(f.read())

# Create quizzes, store them in list so we can use them
# to create quizzes
quizzes_in_db = []
for quiz in quizquestions_data:
    question, answer_choice_1, answer_choice_2,answer_choice_3, answer_choice_4= (
        quiz[0],
        quiz[1],
        quiz[2],
        quiz[3],
        quiz[4]
    )
    db_quiz = crud.create_quiz_questions(question, answer_choice_1, answer_choice_2,answer_choice_3, answer_choice_4)
    quizzes_in_db.append(db_quiz)


model.db.session.add_all(quizzes_in_db)
model.db.session.commit()
