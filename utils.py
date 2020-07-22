import string
import random
from bson.errors import InvalidId
from flask import flash
from werkzeug.utils import redirect

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}


def get_random_string():
    """ Gets a random string to use with uploaded images """
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(8))
    return result_str


def catch_me(func, *args, **kwargs):
    """ Catches any exceptions when interacting with the database """
    def wrapper(*args, **kwargs):
        try:
            print("hi")
            return func(**kwargs)
        except bson.errors.InvalidId:
            flash("An error with the database occurred, couldn't find recipe")
            return redirect("error.html", code=302)
        except Exception:
            flash("An error occurred, couldn't handle your request")
            return redirect("error.html", code=302)

    return wrapper


def allowed_file(filename):
    """ Checks the file being uploaded is an image """
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
