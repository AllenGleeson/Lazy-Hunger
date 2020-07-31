import string
import random

""" The allowed image types """
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}


def get_random_string():
    """ Gets a random string to use with uploaded images """
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(8))
    return result_str

def allowed_file(filename):
    """ Checks the file being uploaded is an image """
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
