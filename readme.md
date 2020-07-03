run flask with: python -m flask run

# Lazy Hunger

Lazy hunger is a community based cooking recipe website for people to look up some recipes, create their own and to change or delete recipes on the site.

The aim was to use MongoDB to store recipes and allow users to add their own or update and delete. Also to use Flask to more easily display the recipes back to the user. I use Materialise Framework for the look of the website with some added JS and Jquery to add to the user experience.

Here is a link to the site through github pages: https://allengleeson.github.io/Find-Ireland/

## UX

### Strategy

My goal was to make a website to store some cooking recipes and encourage any users to try or create some easy to make recipes instead of eating more unhealthy food. I didnt want the site to overly focus on health food but instead to push for homecooked food that can be made without much work. Although I want to give difficulty options to the recipes so as the user can make whatever level of recipe they would like.

I want to view recipes, and allow users to create, update and delete recipes.

The website is aimed at people who wish to make something to eat.

#### User Stories

- A new user comes to the website and sees the Home Page
- The home page will display some recipes with some minor details
- Each recipe will have an edit and delete button
- If they click on the recipe then they will be able to view the full recipe
- The user can also choose to create a recipe and will be taken to Create A Recipe page


### Scope

To achieve my goal I need the following:

#### Functional Requirements
    1. The website will have 2 main pages on the navigation, The home page that will display all the recipes and the create a recipe page to show a form to create your own recipe
    2. There will also be a create and edit recipe pages, both with the same form but the edit form will be prefilled
    2. Must display correctly for different devices
    3. Navigation between pages should be clear
    4. I need a database to store the recipes
    5. Clicking on a recipe should bring to a view recipe page
    6. Each recipe will need a edit and delete recipe button
    7. The website will need to be able to create, update and delete recipes from the database

#### Non-Functional Requirements
    1. The website will be clear to use
    2. Give useful information to the user


#### Content Requirements
    1. The website will contain images
    2. A jumbotron
    3. Cards for recipes
    4. A form for creating or editing recipes

### Structure

The goal of the website is for users to be able to view recipes and then edit, delete or create their own recipes so I will need 4 pages

#### Home -
    The Home page will have a jumbotron with and image with some site description at the top. Then a search bar and a dropdown to sort the recipes by the difficulty.
    The recipes will be displayed in cards. Clicking on a recipe will bring you to the View Recipe page for that recipe.
    Clicking on the Edit Button will direct you to the Edit Recipe page.
    And clicking on the Delete Button will display an alert box and ask if you are sure you want to delete that recipe, if yes then it will delete the recipe.

#### View Recipe -
    Clicking on a recipe from the Home Page will display all the recipes information to the user.
    There will also be buttons at the bottom to Edit or Delete the recipe.


#### Edit Recipe -
    The Edit Recipe will diplay a form with that recipes information prefilled in. You will be able to change the image by clicking on the Change Image Button.
    Upon changing the forms fields the user can click on the Update Recipe Button which will update the recipe in the database.
    Or they can click cancel and an alert box will diplay asking the user if they are sure they want to cancel. If yes then the user will be directed back to the Home Page.


#### Create A Recipe -
    The Create A Recipe page will diplay a form for the user to enter their recipe information. You will be add an image by clicking on the Add Image Button.
    Upon adding to the forms fields the user can click on the Create Recipe Button which will create the recipe in the database.
    Or they can click cancel and an alert box will diplay asking the user if they are sure they want to cancel. If yes then the user will be directed back to the Home Page.
    
### Skeleton

I created some wireframes for the website which are in this repository.

### Surface

I tried to style the website based on what colours are assosiated with food and choose a font I thought looked might look like it would be in a fancy cook book.

## Features

The header is created with the Materialise

The about page features a bootstrap carousel to go through a few selected images.
https://getbootstrap.com/docs/4.0/components/carousel/

The recipe cards created on the home page and done with Materialise Cards.
https://getbootstrap.com/docs/4.3/components/card/

I use icons from Maps Icons Collection for the attraction markers on the map.
https://mapicons.mapsmarker.com

Check API Used below for the API used in this website.

## Technologies Used

This project used Materialise, HTML5 & CSS3, JS, Jquery, Python3, Flask and MongoDB.
Github is used for version control and the website is hosted on Heroku.

## Testing

I largely used the browsers DevTools and Visual Studio Codes debug mode to create breakpoints to view what I was changing and to test.

1. Home Page:
    1. Click on marker Image:
        Creates appopiate town and cards below map
    2. Click on town button:
        Creates appopiate town and cards below map

2. About Page:
    1. Click on carosel to next or previous image
    2. Weather forcast is displayed on page start up

Head:
    Navigation buttons bring to correct page
Footer:
    Clicking email will let you create an email

The project was tested in different screen sizes and will be mobile friendly with help from bootstrap.

## Deployment

I added all my code and images to github and then deployed my project through Github Pages.
First going to settings on my respository, then going down to Github Pages and choosing the master branch.
The site was then published with github pages.
https://allengleeson.github.io/Find-Ireland/

### Content
- The content of the home page is all user created and stored on MongoDB then displayed to the user.

### Media

### Future Additions

I am planning to add a chat system so users can talk to eachother. Also a log in system so the users can rate recipes.