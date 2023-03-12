"""CRUD operations."""

from model import db, User, DailyWords, DictionaryWords,DailyQuiz,QuizQuestions,ClaimedRewards,Rewards,NotePage,BooksPodcasts,ResourcePageNextSteps, connect_to_db

def create_user(first_name, last_name , email,age_input, password):
    """Create and return a new user."""

    user = User(first_name=first_name, last_name=last_name , email=email,age_input=age_input, password=password)
    db.session.add(user)
    db.session.commit()

    return user

def create_wordofday(datetime, user_id , dict_key_id,finished_true_false):
    """Create and return word of the day."""

    wordofday = DailyWords(datetime=datetime, user_id = user_id, dict_key_id = dict_key_id,finished_true_false = finished_true_false)
    db.session.add(wordofday)
    db.session.commit()

    return wordofday

def create_dictionary_words(definition, age_input ):
    """Create and return dictionary words."""

    dictionary_words = DictionaryWords(definition = definition, age_input = age_input)
    db.session.add(dictionary_words)
    db.session.commit()
    return dictionary_words 

def create_daily_quiz_of_day (user_id , datetime, finished_true_false,correct_true_false):
    """Create and return daily quiz of the day."""

    daily_quiz_of_day = DailyQuiz(user_id = user_id, datetime = datetime, finished_true_false=finished_true_false,correct_true_false=correct_true_false)
    db.session.add(daily_quiz_of_day)
    db.session.commit()
    return daily_quiz_of_day

def create_quiz_questions(question,answer_choice_1 ,answer_choice_2,answer_choice_3, answer_choice_4):
    """Create and return quiz questions."""

    quiz_questions = QuizQuestions(question=
    question,
    answer_choice_1=answer_choice_1,
    answer_choice_2=answer_choice_2,
    answer_choice_3=answer_choice_3,
    answer_choice_4=answer_choice_4 )
    
    return quiz_questions

def create_claimed_rewards(user_id , rewards, datetime,claimed_true_false):
    """Create and return claimed rewards."""

    claimed_rewards = ClaimedRewards(user_id = user_id, rewards = rewards, datetime = datetime,claimed_true_false = claimed_true_false)
    db.session.add(claimed_rewards)
    db.session.commit()
    return claimed_rewards


def create_rewards(title, description):
    """Create and return rewards."""

    rewards = Rewards(title = title, description = description)
    db.session.add(rewards)
    db.session.commit()
    return rewards


def create_notepage(user_id, note):
    """Create and return notepage."""

    notepage = NotePage(user_id = user_id , note = note)
    db.session.add(notepage)
    db.session.commit()
    return notepage


def create_booksnpodcasts(user_id, title, description, read_if_you_based_on_interests):
    """Create and return notepage."""

    booksnpodcasts = BooksPodcasts(user_id = user_id , title = title, description = description, read_if_you_based_on_interests= read_if_you_based_on_interests)
    db.session.add(booksnpodcasts)
    db.session.commit()
    return booksnpodcasts



def create_nextsteps(resource_name, url,resource_description ):
    """Create and return notepage."""

    nextsteps = ResourcePageNextSteps(resource_name = resource_name, url = url, resource_description = resource_description)
    db.session.add(nextsteps)
    db.session.commit()
    return nextsteps


def get_users():
    """Return all users."""

    return User.query.all()


def get_user_by_id(user_id):
    """Return a user by primary key."""

    return User.query.get(user_id)


def get_user_by_email(email):
    """Return a user by email."""

    return User.query.filter(User.email == email).first()


if __name__ == "__main__":
    from server import app

    connect_to_db(app)
