/* Nav */

$(document).ready(function () {
  $('.sidenav').sidenav();
});

$('.dropdown-trigger').dropdown();

$("#add_ingredient").click(function () {
  add_ingredient();
});

$("#add_cooking_method").click(function () {
  add_cooking_method();
});

$(".deleteListItem").click(function () {
  $(this).closest('li').remove();
});


function add_ingredient() {

  let ingredientText = document.getElementById("ingredient");
  let ingredientsList = document.getElementsByClassName("ingredients-list");

  let ingredientlistItem = document.createElement('li');
  let ingredient = document.createElement('p');
  let ingredientHiddenInput = document.createElement('input');

  let deleteIngredientButton = document.createElement('button');
  let iconDiv = document.createElement('div');
  let deleteIcon = document.createElement('i');

  cookingMethod.innerText(methodText.value());

  ingredientHiddenInput.setAttribute("type", "hidden");
  ingredientHiddenInput.setAttribute("name", "methods");
  ingredientHiddenInput.setAttribute("value", ingredientText.value());

  deleteIcon.setAttribute("class", "small material-icons");
  deleteIcon.innerText("delete");



  iconDiv.appendChild(deleteIcon);
  deleteIngredientButton.appendChild(iconDiv);

  ingredientlistItem.appendChild(ingredient);
  ingredientlistItem.appendChild(ingredientHiddenInput);
  ingredientlistItem.appendChild(iconDiv);

  ingredientsList[0].appendChild(ingredientlistItem);
  
}

// Create the city description above the cards
function add_cooking_method() {

  let methodText = document.getElementById("method");
  let cookingMethodsList = document.getElementsByClassName("cooking-methods-list");

  let methodlistItem = document.createElement('li');
  let cookingMethod = document.createElement('p');
  let methodHiddenInput = document.createElement('input');

  let deleteMethodButton = document.createElement('button');
  let iconDiv = document.createElement('div');
  let deleteIcon = document.createElement('i');

  cookingMethod.innerText(methodText.value());

  methodHiddenInput.setAttribute("type", "hidden");
  methodHiddenInput.setAttribute("name", "methods");
  methodHiddenInput.setAttribute("value", methodText.value());

  deleteIcon.setAttribute("class", "small material-icons");
  deleteIcon.innerText("delete");



  iconDiv.appendChild(deleteIcon);
  deleteMethodButton.appendChild(iconDiv);

  methodlistItem.appendChild(cookingMethod);
  methodlistItem.appendChild(methodHiddenInput);
  methodlistItem.appendChild(iconDiv);

  cookingMethodsList[0].appendChild(methodlistItem);
  
}