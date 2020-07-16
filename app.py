import os
import base64
import random
import string
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'lazy-hunger'
app.config["MONGO_URI"] = os.getenv('DBConnectionString')
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

mongo = PyMongo(app)

@app.route('/')
@app.route('/get_recipes/')
def get_recipes():
    sort = request.args.get('sort')
    search = request.args.get('search')
    recipes= ""

    print(search)
    print(sort)
    if search and len(search) > 0:
        recipes = mongo.db.recipes.find( { "recipe_name" : { "$regex" : ".*" + search + ".*"}} )
    else:
        recipes=mongo.db.recipes.find()
    
    if sort:
        if sort == "difficulty":
            recipes = recipes.sort({ sort : -1 })
        elif sort == "recipe_name":
            recipes = recipes.sort({ sort : -1 })
        elif sort == "time":
            recipes = recipes.sort({ "cooking_time" : -1, "prep_time" : -1})
        elif sort == "serves":
            recipes = recipes.sort({ sort : -1 })

    return render_template("index.html", recipes=recipes)

@app.route('/add_recipe')
def add_recipe():
    return render_template('create_recipe.html')


@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    recipes =  mongo.db.recipes

    print(request.form)
    print(request.form.getlist('methods'))
    print(request.files)

    image = request.files['image']
    path = ""
    if image and allowed_file(image.filename):
        path = "static/images/" + get_random_string() + image.filename
        image.save(path)

    recipes.insert_one(
        {
        'recipe_name':request.form.get('recipe_name'),
        'recipe_description':request.form.get('description'),
        'prep_time': request.form.get('prep_time'),
        'cooking_time': request.form.get('cooking_time'),
        'difficulty':request.form.get('difficulty'),
        'serves':request.form.get('serves'),
        'recipe_image': "/" + path,
        'ingredients':request.form.getlist('ingredients'),
        'methods':request.form.getlist('methods')
    }
    )
    return redirect(url_for('get_recipes'))

@app.route('/view_recipe/<recipe_id>')
def view_recipe(recipe_id):
    print(recipe_id)
    recipe =  mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template('view_recipe.html', recipe=recipe)

@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    recipe =  mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template('edit_recipe.html', recipe=recipe)

@app.route('/update_recipe/<recipe_id>', methods=["POST"])
def update_recipe(recipe_id):
    recipes = mongo.db.recipes

    image = request.files['image']
    path = ""
    if image and allowed_file(image.filename):
        path = "static/images/" + get_random_string() + image.filename
        image.save(path)

    current_image = recipes.find_one({'_id': ObjectId(recipe_id)})
    print("Current image file:")
    print(current_image)
    print("Current image:")
    print(current_image['recipe_image'])
    os.remove("."+current_image['recipe_image'])
    
    recipes.update( {'_id': ObjectId(recipe_id)},
    {
        'recipe_name':request.form.get('recipe_name'),
        'recipe_description':request.form.get('description'),
        'prep_time': request.form.get('prep_time'),
        'cooking_time': request.form.get('cooking_time'),
        'difficulty':request.form.get('difficulty'),
        'serves':request.form.get('serves'),
        'recipe_image': "/" + path,
        'ingredients':request.form.getlist('ingredients'),
        'methods':request.form.getlist('methods')
    }
    )

    return redirect(url_for('get_recipes'))


@app.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({'_id': ObjectId(recipe_id)})
    return redirect(url_for('get_recipes'))


""" Checks the file being uploaded is an image """
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

""" Gets a random string to use with uploaded images """
def get_random_string():
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(8))
    return result_str


if __name__ == '__main__':
    """ app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True """
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')))