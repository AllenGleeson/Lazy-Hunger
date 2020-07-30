import os
import bson
import pymongo
from flask import Flask, render_template, redirect, request, url_for, flash
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

from utils import catch_me, get_random_string, allowed_file

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'lazy-hunger'
app.config["MONGO_URI"] = os.getenv('DBConnectionString')
mongo = PyMongo(app)


@catch_me
@app.route('/')
@app.route('/get_recipes/')
def get_recipes():
    sort_key = request.args.get('sort')
    search = request.args.get('search')

    if not sort_key:
        sort_key = "recipe_name"

    recipe_count = mongo.db.recipes.find().count()

    recipes = mongo.db.recipes.find().collation({"locale": "en"}) if not search else mongo.db.recipes.find(
        {"recipe_name": {"$regex": "(?i).*" + search + ".*"}}).collation({"locale": "en"})

    if sort_key == "difficulty" or sort_key == "recipe_name" or sort_key == "serves" or sort_key == "total_time":
        recipes = recipes.sort(sort_key, pymongo.ASCENDING)

    print(recipes)
    return render_template("index.html", recipes=recipes, recipe_count=recipe_count)


@catch_me
@app.route('/add_recipe')
def add_recipe():
    return render_template('create_recipe.html')


@catch_me
@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    recipes = mongo.db.recipes
    image = request.files['image']
    path = ""

    if image and allowed_file(image.filename):
        path = "static/images/" + get_random_string() + image.filename
        image.save(path)

    prep_time = int(request.form.get('prep_time'))
    cooking_time = int(request.form.get('cooking_time'))
    total_time = prep_time + cooking_time

    recipes.insert_one(
        {
            'recipe_name': request.form.get('recipe_name'),
            'recipe_description': request.form.get('description'),
            'prep_time': prep_time,
            'cooking_time': cooking_time,
            'total_time': total_time,
            'difficulty': request.form.get('difficulty'),
            'serves': request.form.get('serves'),
            'recipe_image': f"/{path}" if path else None,
            'ingredients': request.form.getlist('ingredients'),
            'methods': request.form.getlist('methods')
        }
    )
    return redirect(url_for('get_recipes'))


@catch_me
@app.route('/view_recipe/<recipe_id>')
def view_recipe(recipe_id):

    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template('view_recipe.html', recipe=recipe)


@catch_me
@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template('edit_recipe.html', recipe=recipe)


@catch_me
@app.route('/update_recipe/<recipe_id>', methods=["POST"])
def update_recipe(recipe_id):
    recipes = mongo.db.recipes

    image = request.files['image']
    path = ""

    prep_time = int(request.form.get('prep_time'))
    cooking_time = int(request.form.get('cooking_time'))
    total_time = prep_time + cooking_time

    if image and allowed_file(image.filename):
        path = "static/images/" + get_random_string() + image.filename
        image.save(path)

        current_recipe = recipes.find_one({'_id': ObjectId(recipe_id)})
        current_image = current_recipe['recipe_image']

        if current_image and os.path.exists("." + current_image):
            os.remove("." + current_image)

        recipes.update({'_id': ObjectId(recipe_id)},
                    {
                        'recipe_name': request.form.get('recipe_name'),
                        'recipe_description': request.form.get('description'),
                        'prep_time': prep_time,
                        'cooking_time': cooking_time,
                        'total_time': total_time,
                        'difficulty': request.form.get('difficulty'),
                        'serves': request.form.get('serves'),
                        'recipe_image': "/" + path,
                        'ingredients': request.form.getlist('ingredients'),
                        'methods': request.form.getlist('methods')
                    }
                    )
    else:
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

    return redirect(url_for('get_recipes'))


@catch_me
@app.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
    recipes = mongo.db.recipes
    current_recipe = recipes.find_one({'_id': ObjectId(recipe_id)})
    current_image = current_recipe['recipe_image']

    if current_image and os.path.exists("." + current_image):
        os.remove("." + current_image)
        mongo.db.recipes.remove({'_id': ObjectId(recipe_id)})
    else:
        mongo.db.recipes.remove({'_id': ObjectId(recipe_id)})
    return redirect(url_for('get_recipes'))


if __name__ == '__main__':
    """ app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True """
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT'), ))
