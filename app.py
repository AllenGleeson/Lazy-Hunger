import os
import bson
import pymongo
from pymongo import errors
from flask import Flask, render_template, redirect, request, url_for, flash
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from bson.errors import InvalidId
from utils import get_random_string, allowed_file
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
app.config["MONGO_URI"] = os.environ.get("DBConnectionString")
app.secret_key = os.environ.get("secret_key")
mongo = PyMongo(app)

@app.errorhandler(500)
@app.errorhandler(InvalidId)
@app.errorhandler(errors.ConnectionFailure)
@app.errorhandler(errors.CursorNotFound)
def handle_bad_request(e):
    """ Error handling: will catch these errors and display the play messages to error.html """
    if type(e) is InvalidId:
        flash("We dont have this recipe anymore.")
    if type(e) is errors.ConnectionFailure:
        flash("Having troubles connecting right now. Please try again later.")
    if type(e) is errors.CursorNotFound:
        flash("Sorry a problem on our side.")
    
    return render_template("/error.html")


@app.errorhandler(Exception)
def handle_other_errors(e):
    """ Default error handling for other exceptions """
    flash("An unexpected error occurred.")
    return render_template("error.html")


@app.route('/')
@app.route('/get_recipes/')
def get_recipes():
    """ A View for the Home Page """
    """ Sets the search and sort """
    sort_key = request.args.get('sort')
    search = request.args.get('search')
    
    """ If there is no sort key then the sort will be set to the name """
    if not sort_key:
        sort_key = "recipe_name"

    """ Gets the recipes count to determine if there are any entries in the database """
    recipe_count = mongo.db.recipes.count()
    print("Recipe count+++++++++++++++",recipe_count)
    """ If search is empty then it will return all entries in the database
    But if there is a search then it will return entries where the recipe name contains that search """
    recipes = mongo.db.recipes.find().collation({"locale": "en"}) if not search else mongo.db.recipes.find(
        {"recipe_name": {"$regex": "(?i).*" + search + ".*"}}).collation({"locale": "en"})

    """ Checks if the sort key is one of the available selected and sorts in ascending order """
    if sort_key == "difficulty" or sort_key == "recipe_name" or sort_key == "serves" or sort_key == "total_time":
        recipes = recipes.sort(sort_key, pymongo.ASCENDING)

    return render_template("index.html", recipes=recipes, recipe_count=recipe_count)


@app.route('/add_recipe')
def add_recipe():
    """ A View for the Create Recipe Page """
    return render_template('create_recipe.html')


@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    """ When the user clicks to add the new recipe """
    recipes = mongo.db.recipes
    image = request.files['image']
    path = ""

    """ Checks if there is an image and if that image is of the allowed filetype """
    if image and allowed_file(image.filename):
        """ Sets the path with the image and a random string to make it unique, then saves the image to that path """
        path = "static/images/" + get_random_string() + image.filename
        image.save(path)

    """ Takes the prep_time and cooking_time from the form as integers then adds them together to get the total time """
    prep_time = int(request.form.get('prep_time'))
    cooking_time = int(request.form.get('cooking_time'))
    total_time = prep_time + cooking_time

    """ Takes the required fields from the form and makes a new entry to the database """
    """ Sets the image to the path if the image exists and is allowed, if not it will set the image to none """
    recipes.insert_one(
        {
            'recipe_name': request.form.get('recipe_name'),
            'recipe_description': request.form.get('description'),
            'prep_time': prep_time,
            'cooking_time': cooking_time,
            'total_time': total_time,
            'difficulty': request.form.get('difficulty'),
            'serves': request.form.get('serves'),
            'recipe_image': f"{path}" if path else None,
            'ingredients': request.form.getlist('ingredients'),
            'methods': request.form.getlist('methods')
        }
    )
    """ Once created redirects to the Home Page """
    return redirect(url_for('get_recipes'))


@app.route('/view_recipe/<recipe_id>')
def view_recipe(recipe_id):
    """ A View for the View Recipe Page """
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template('view_recipe.html', recipe=recipe)


@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    """ A View for the Edit Recipe Page """
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template('edit_recipe.html', recipe=recipe)


@app.route('/update_recipe/<recipe_id>', methods=["POST"])
def update_recipe(recipe_id):
    """ When the user clicks to update the recipe """
    recipes = mongo.db.recipes
    image = request.files['image']
    path = ""

    """ Takes the prep_time and cooking_time from the form as integers then adds them together to get the total time """
    prep_time = int(request.form.get('prep_time'))
    cooking_time = int(request.form.get('cooking_time'))
    total_time = prep_time + cooking_time

    """ Gets the current image path """
    current_recipe = recipes.find_one({'_id': ObjectId(recipe_id)})
    current_image = current_recipe['recipe_image']

    """ Checks if there is an image and if that image is of the allowed filetype """
    if image and allowed_file(image.filename):
        """ Sets the path with the image and a random string to make it unique, then saves the image to that path """
        path = "static/images/" + get_random_string() + image.filename
        image.save(path)


        """ Checks if that image path exists on the server - If it does then it deletes it """
        if current_image and os.path.exists("." + current_image):
            os.remove("./" + current_image)

        """ Updates the recipe """
        recipes.update({'_id': ObjectId(recipe_id)},
                    {
                        'recipe_name': request.form.get('recipe_name'),
                        'recipe_description': request.form.get('description'),
                        'prep_time': prep_time,
                        'cooking_time': cooking_time,
                        'total_time': total_time,
                        'difficulty': request.form.get('difficulty'),
                        'serves': request.form.get('serves'),
                        'recipe_image': path,
                        'ingredients': request.form.getlist('ingredients'),
                        'methods': request.form.getlist('methods')
                    }
                    )
    else:

        path = current_image
        """ Updates the recipe """
        recipes.update({'_id': ObjectId(recipe_id)},
                    {
                        'recipe_name': request.form.get('recipe_name'),
                        'recipe_description': request.form.get('description'),
                        'prep_time': prep_time,
                        'cooking_time': cooking_time,
                        'total_time': total_time,
                        'difficulty': request.form.get('difficulty'),
                        'serves': request.form.get('serves'),
                        'recipe_image': path,
                        'ingredients': request.form.getlist('ingredients'),
                        'methods': request.form.getlist('methods')
                    }
                    )
    """ Redirects back to the Home Page """
    return redirect(url_for('get_recipes'))


@app.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
    """ When the user clicks to delete a recipe """

    """ Gets the current image path """
    recipes = mongo.db.recipes
    current_recipe = recipes.find_one({'_id': ObjectId(recipe_id)})
    current_image = current_recipe['recipe_image']

    """ Checks if that image path exists on the server - If it does then it deletes it and the recipe """
    """ If the image doesnt exist then it will just delete the recipe """
    if current_image and os.path.exists("." + current_image):
        os.remove("./" + current_image)
        mongo.db.recipes.remove({'_id': ObjectId(recipe_id)})
    else:
        mongo.db.recipes.remove({'_id': ObjectId(recipe_id)})
    return redirect(url_for('get_recipes'))

""" Sets the apps host and port """
if __name__ == "__main__":
    app.run(debug=False)