import os
import base64
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId 

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'lazy-hunger'
app.config["MONGO_URI"] = os.getenv('DBConnectionString')

mongo = PyMongo(app)

#render_template("index.html", recipes=mongo.db.recipes.find())
@app.route('/')
@app.route('/get_recipes/')
def get_recipes():
    print(search_string)
    if search_string:
        recipes = mongo.db.recipes.find( { recipe_name: search_string } )
    else:
        print(mongo.db.recipes.find())
        recipes=mongo.db.recipes.find()

    return render_template("index.html", recipes)

@app.route('/add_recipe')
def add_recipe():
    return render_template('create_recipe.html')


@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    recipes =  mongo.db.recipes

    print(request.form)
    print(request.form.getlist('methods'))
    print(request.files)
    recipes.insert_one(
        {
        'recipe_name':request.form.get('recipe_name'),
        'recipe_description':request.form.get('description'),
        'prep_time': request.form.get('prep_time'),
        'cooking_time': request.form.get('cooking_time'),
        'difficulty':request.form.get('difficulty'),
        'serves':request.form.get('serves'),
        'recipe_image': "data:image/png;base64," + base64.b64encode(request.files['image'].read()).decode("UTF-8"),
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
    print(recipe_id)
    recipe =  mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    print(recipe)
    return render_template('edit_recipe.html', recipe=recipe)

""" @app.route('/update_recipe/<recipe_id>', methods=["POST"])
def update_recipe(recipe_id):
    recipes = mongo.db.recipes
    recipe_image = mongo.db.recipe_images

    recipes.update( {'_id': ObjectId(recipe_id)},
    {
        'recipe_name':request.form.get('recipe_name'),
        'recipe_description':request.form.get('recipe_description'),
        'prep_time': request.form.get('prep_time'),
        'cooking_time': request.form.get('cooking_time'),
        'difficulty':request.form.get('difficulty'),
        'serves':request.form.get('serves'),
        'recipe_image':request.form.get('recipe_image'),
        'ingrediants':request.form.get('ingrediants')
        'methods':request.form.get('methods')
        'image':request.files["image"]
        base64.b64encode(image_file.read())
    })

    return redirect(url_for('get_recipes')) """


@app.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({'_id': ObjectId(recipe_id)})
    return redirect(url_for('get_recipes'))

if __name__ == '__main__':
    """ app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True """
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')))