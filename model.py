"""Models for Capstone Application."""

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import json
from json import JSONEncoder

db = SQLAlchemy()
class User(db.Model):
    """A user."""

    __tablename__ = 'users'

    user_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    email = db.Column(db.String)
    age_input = db.Column(db.String)
    password = db.Column(db.String)
    claimed_rewards = db.relationship("ClaimedRewards", back_populates="users") #backpopulate on column 
    note_page = db.relationship("NotePage", back_populates="user")
    word_of_day = db.relationship("DailyWords", back_populates="user")
    quiz_of_day = db.relationship("DailyQuiz", back_populates="users")
    def __repr__(self):
        return f'<User user_id={self.user_id} email={self.email} firstname={self.first_name} lastname={self.last_name}>'

class DailyWords(db.Model):
    """Daily word of the day."""

    __tablename__ = 'daily_word_of_day'

    word_of_day_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))
    dict_key_id = db.Column(db.String, db.ForeignKey("dictionary_words.dict_key_id"))
    datetime = db.Column(db.DateTime)
    finished_true_false = db.Column(db.Boolean, default = True)
    dictionary_words = db.relationship("DictionaryWords", back_populates="word_of_day") 
    user = db.relationship("User", back_populates="word_of_day") 
    def __repr__(self):
        return f'<User user_id={self.user_id} datetime={self.datetime} firstname={self.dict_key_id} finished_true_false={self.finished_true_false}>'
    
class DictionaryWords(db.Model):
    """A Dictionary of Words."""

    __tablename__ = 'dictionary_words'
    dict_key_id = db.Column(db.String,primary_key=True)
    definition = db.Column(db.String)
    age_input = db.Column(db.Integer)
    word_of_day = db.relationship("DailyWords", back_populates="dictionary_words")
    def __repr__(self):
        return f'<dict_key={self.dict_key_id} definition={self.definition} age_input= {self.age_input}>'
    
class DailyQuiz(db.Model):
    """daily quiz of the day."""
    __tablename__ = 'daily_quiz_of_day'
    quiz_of_day_id = db.Column(db.Integer,autoincrement=True,primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))
    datetime = db.Column(db.DateTime)
    finished_true_false = db.Column(db.Boolean) 
    correct_true_false = db.Column(db.Boolean) 
    users = db.relationship("User", back_populates="quiz_of_day") 
    quiz_questions = db.relationship("QuizQuestions", back_populates="quiz_of_day") 
    def __repr__(self):
        return f'<User user_id={self.user_id} datetime={self.datetime} quiz_id={self.quiz_id} finished_true_false={self.finished_true_false}>'


class QuizQuestions(db.Model):
    """quiz questins."""

    __tablename__ = 'quiz_questions'

    quiz_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    quiz_of_day_id = db.Column(db.Integer, db.ForeignKey("daily_quiz_of_day.quiz_of_day_id")) 
    question = db.Column(db.String)
    answer_choice_1 = db.Column(db.String)
    answer_choice_2 = db.Column(db.String)
    answer_choice_3 = db.Column(db.String)
    answer_choice_4 = db.Column(db.String)
    correct_answer_reasoning = db.Column(db.String)
    incorrect_answer_feedback = db.Column(db.String)
    age_input = db.Column(db.Integer)
    quiz_of_day = db.relationship("DailyQuiz", back_populates="quiz_questions") 
    def __repr__(self):
        return f'<quiz_id={self.quiz_id} question={self.question} answer_choice_1 = {self.answer_choice_1} answer_choice_2 = {self.answer_choice_2} correct_answer_reasoning= {self.correct_answer_reasoning} incorrect_answer_feedback = {self.incorrect_answer_feedback}  age_input = {self.age_input}>'

class ClaimedRewards(db.Model):
    """A user."""

    __tablename__ = 'claimed_rewards'

    claimed_rewards_id = db.Column(db.Integer,
    autoincrement=True,
    primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))
    rewards_id = db.Column(db.Integer, db.ForeignKey("rewards.rewards_id"))
    datetime = db.Column(db.DateTime)
    claimed_true_false = db.Column(db.Boolean) 
    users = db.relationship("User", back_populates="claimed_rewards") 
    rewards = db.relationship("Rewards", back_populates="claimed_rewards") 
    def __repr__(self):
        return f'<User user_id={self.user_id} datetime={self.datetime} firstname={self.dict_key_id} finished_true_false={self.finished_true_false}>'
    
class Rewards(db.Model):
    """A user."""

    __tablename__ = 'rewards'
    rewards_id = db.Column(db.Integer,
    autoincrement=True,
    primary_key=True)
    title = db.Column(db.String)
    description = db.Column(db.String)
    claimed_rewards = db.relationship("ClaimedRewards", back_populates="rewards") 
    def __repr__(self):
        return f'< rewards_id={self.rewards_id} title={self.title} description={self.description}>'
    
class NotePage(db.Model):
    """A user."""

    __tablename__ = 'note_page'
    note_id = db.Column(db.Integer,
    autoincrement=True,
    primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))
    note = db.Column(db.Text)
    user = db.relationship("User", back_populates="note_page")  
    def __repr__(self):
        return f'< note_id={self.note_id} user_id ={self.user_id} note={self.note}>'
    
class BooksPodcasts(db.Model):
    """A user."""

    __tablename__ = 'books_podcasts'

    books_podcasts_id = db.Column(db.Integer,
    autoincrement=True,
    primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))
    title = db.Column(db.String)
    description = db.Column(db.String)
    read_if_you_based_on_interests = db.Column(db.String)
    def __repr__(self):
        return f'user_id ={self.user_id} title={self.title} description = {self.description} read if you are interested in {self.read_if_you_based_on_interests}>'

class ResourcePageNextSteps(db.Model):
    """A user."""
    __tablename__ = 'next_steps_resources'
    next_steps_resources_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    resource_name = db.Column(db.String)
    url = db.Column(db.String)
    resource_description = db.Column(db.String)
    def __repr__(self):
        return f'next_steps_resources_id ={self.next_steps_resources_id} resource_name ={self.resource_name} resource_description = {self.resource_description} url {self.url}>'
    

def connect_to_db(flask_app, db_uri="postgresql:///apptest", echo=True):  #update later 
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the db!")


if __name__ == "__main__":
    from server import app
    connect_to_db(app)
