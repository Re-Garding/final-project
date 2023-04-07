"""Script to seed database."""

import os
import json
import crud
import model
import server

os.system("dropdb apptest")
os.system("createdb apptest")

model.connect_to_db(server.app)
model.db.create_all()

with open("data/users.json") as f:
    users_data = json.loads(f.read())

with open("data/rewards.json") as f:
    rewards_data = json.loads(f.read())

with open("data/quizquestions.json") as f:
    quizquestions_data = json.loads(f.read())

with open("data/next_steps.json") as f:
    next_steps_data = json.loads(f.read())

with open("data/dictionary.json") as f:
    dictionary_data = json.loads(f.read())

with open("data/books_podcasts.json") as f:
    books_podcasts_data = json.loads(f.read())

for word in dictionary_data:
    dict_key_id, definition, age_input = (
        word["word"],
        word["def"],
        word["age"]
    )
    crud.create_dictionary_words(dict_key_id, definition, age_input)

for step in next_steps_data:
    name, url, resource = (
        step["resource_name"],
        step["url"],
        step["resource_description"]
    )
    crud.create_nextsteps(name, url, resource)

for reward in rewards_data:
    title, description = (
        reward["title"],
        reward["description"]
    )
    crud.create_rewards(title, description)

for user in users_data:
    fname, lname,email,age_input,password = (
        user["first_name"],
        user["last_name"],
        user["email"],
        user["age_input"],
        user["password"]
    )
    new_user = crud.create_user(fname,lname,email,age_input,password)

user_ids = 1
for book in books_podcasts_data:
    title, description, read_if_you_based_on_interests = (
        book["title"],
        book["description"],
        book["interest"]
    ) 
    crud.create_booksnpodcasts(user_ids, title, description, read_if_you_based_on_interests)
    user_ids += 1
   
quizzes_in_db = []
for quiz in quizquestions_data:
    question, answer_choice_1, answer_choice_2,answer_choice_3, answer_choice_4, correct_answer_reasoning, incorrect_answer_feedback, age_input = (
        quiz["question"],
        quiz["answer_choice_1"],
        quiz["answer_choice_2"],
        quiz["answer_choice_3"],
        quiz["answer_choice_4"],
        quiz["correct_answer_reasoning"],
        quiz["incorrect_answer_feedback"],
        quiz["age_input"]
    )
    db_quiz = crud.create_quiz_questions(question, answer_choice_1, answer_choice_2,answer_choice_3, answer_choice_4, correct_answer_reasoning, incorrect_answer_feedback, age_input)
    quizzes_in_db.append(db_quiz)

model.db.session.add_all(quizzes_in_db)
model.db.session.commit()
