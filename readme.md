# Lazy Hunger

Lazy hunger is a community based cooking recipe website for people to look up some recipes, create their own and to change or delete recipes on the site.

The aim was to use MongoDB to store recipes and allow users to add their own or update and delete. Also to use the Flask framework to display the recipes back to the user. I use Materialise Framework for the look of the website with some added JS and Jquery to add to the user experience.

Here is a link to the published site on Heroku: https://lazy-hunger.herokuapp.com/

## UX

### Strategy

My goal was to make a website to store some cooking recipes and encourage any users to try or create some easy to make recipes instead of eating more unhealthy food. I didnt want the site to overly focus on health food but instead to push for homecooked food that can be made without much work. Although I want to give difficulty options to the recipes so as the user can make whatever level of recipe they would like.

I want to view recipes, and allow users to create, update and delete recipes.
I also want users to be able to search through the current recipes.

The website is aimed at people who wish to make something to eat.

#### User Stories

- A user looking for something to cook:
Arrives on home page.
Sees recipes.
Can Search or sort recipes.
Clicks on a recipe that interests them and is taken to the View Recipe Page.
On recipe page the user is displayed the recipes further details.

- A user wants to create a recipe:
Arrives on the home page.
Clicks Create Recipe on the navigation.
A form is displayed on the Create Recipe Page.
User can then input a recipe image, name, description, cooking time, difficulty and how many it serves.
User can then add ingredients and cooking methods.
Click Create to add recipe to the database then be redirected to home page or Cancel to return to the Home page..

- A user wants to edit a recipe:
They can click the edit recipe button on the Home or View Recipe pages.
When clicked they will be taken to the Edit Recipe page with a prefilled form then can edit.
Click Update to update the recipe or Cancel to return to the Home page.

- A user wants to delete a recipe
They can click the delete recipe button on the Home or View Recipe pages.
When clicked the recipe will be deleted and the page refreshed.




### Scope

To achieve my goal I need the following:

#### Functional Requirements
    1. The website will have 2 main pages on the navigation, The home page that will display all the recipes and the create a recipe page to show a form to create your own recipe
    2. There will also be a View and Edit Recipe pages. The View page will display the recipe details and Edit recipe will display a prefilled form.
    3. Must display correctly for different screen sizes and devices.
    4. Navigation between pages should be clear
    5. I need a database to store the recipes
    6. Clicking on a recipe should bring to a view recipe page
    7. Each recipe will need a edit and delete recipe button
    8. The website will need to be able to create, update and delete recipes from the database

#### Non-Functional Requirements
    1. The website will be clear to use
    2. Give useful information to the user


#### Content Requirements
    1. MongoDB to store the data
    2. The website will contain images
    3. A jumbotron
    4. Cards for recipes
    5. A form for creating or editing recipes

### Structure

The goal of the website is for users to be able to view recipes they could try,edit, delete or create their own recipes so I will need 4 pages

#### Home -
    The Home page will have a jumbotron with and image with some site description at the top. Then a search bar and a dropdown to sort the recipes by the Name, How many people the meal serves, how long it takes to cook and how difficult is it.
    The recipes will be displayed in cards.
    Clicking on a recipe will bring you to the View Recipe page for that recipe.
    Clicking on the Edit Button will direct you to the Edit Recipe page.
    And clicking on the Delete Button will display an alert box and ask if you are sure you want to delete that recipe, if yes then it will delete the recipe.

#### View Recipe -
    Clicking on a recipe from the Home Page will display all the recipes information to the user.
    An Image, Name, Description, Cooking Time, Preparation Time, Difficulty, Ingredients and Cooking Methods.
    There will also be buttons at the bottom to Edit or Delete the recipe.


#### Edit Recipe -
    The Edit Recipe will diplay a form with that recipes information prefilled in. You will be able to change the image by clicking on the Change Image Button.
    Upon changing the forms fields the user can click on the Update Recipe Button which will update the recipe in the database.
    Or they can click cancel and the user will be directed back to the Home Page.


#### Create A Recipe -
    The Create A Recipe page will diplay a form for the user to enter their recipe information. You will be add an image by clicking on the Add Image Button.
    Upon adding to the forms fields the user can click on the Create Recipe Button which will create the recipe in the database.
    Or they can click cancel and the user will be directed back to the Home Page.
    
### Skeleton

I created some wireframes for the website which are in this repository.

### Surface

The font I chose because I thought it looked like it could be found in a cook book. The colors I chose are based on other recipe websites and research on what colors people assiosiate with food. A crimson red for the navigation and buttons and a baige color for the recipe cards and background for the top half of the other pages.
Horizontal cards from Materialise with images are used for the Home page. A recipes page is diveded into two rows to try to keep things self contained and easy for the user to understand.

## Features

I get the following from Materialise:
https://materializecss.com/

Grid System
https://materializecss.com/grid.html

Side Nav for Mobile
https://materializecss.com/mobile.html

The recipe cards created on the home page.
https://materializecss.com/cards.html

Icons
https://materializecss.com/icons.html

Select, used on the edit and create pages
https://materializecss.com/select.html

Forms, used on edit and create pages
https://materializecss.com/text-inputs.html

## Technologies Used

This project used Materialise, HTML5 & CSS3, JS, Jquery, Python3, Flask and MongoDB.
Github is used for version control and the website is hosted on Heroku.

## Testing

I largely used the browsers DevTools and Visual Studio Codes debug mode to create breakpoints to view what I was changing and to test.
The project was tested in different screen sizes and will be mobile friendly with help from Materialise.

Below I have some manual testing done through the site:
https://github.com/AllenGleeson/Lazy-Hunger/tree/master/Testing

## Deployment

I added all my code and images to github and then deployed my project through Heroku.
Going ot Heroku and creating a new Heroku App with the projects name. Then connecting the app to the code on github and doing a
manual deploy, ensuring to have the Procile and requirements.txt required to run the project on Heroku.
https://devcenter.heroku.com/articles/github-integration

Site is published at: https://lazy-hunger.herokuapp.com/

### Content

- There is an image for the jumbotron on the Home Page and the rest of the content of the home page is all user created and stored on MongoDB then displayed to the user.

### Media

Media will be user added.

### Future Additions

I am planning to add a chat system so users can talk to eachother. Also a log in system so the users can rate recipes.
Before that though I will add some alert boxes so users can be alerted before they create, update or delete a recipe.
