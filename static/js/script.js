

/* On Document Ready */
/* Inistialises the sidenav and select options */
$(document).ready(function () {
  $('.sidenav').sidenav();
  $('select').formSelect();
});

/* Form validation */
/* Prevents the form from being submitted then checks if there has been any ingredients or cooking methods AudioDestinationNode. If not then it will display an error. */
$("form").submit(function( e ) {
  
  if(!$(".ingredients-list").children().length){
    $(".ingredients span").text("No ingedients added");
    e.preventDefault();
  }

  if(!$(".cooking-methods-list").children().length){
    $(".cooking_methods span").text("No ingedients added");
    e.preventDefault();
  }

});

/* Prevents any empty ingredients or cooking methods from being created */
/* If the input is not empty then it will create the new ingredient or cooking method using add_item()*/
$("#add_ingredient").click(function () {
  if(!$("#ingredient").val()){
    $(".ingredients span").text("Ingredient must have a name");
    return;
  }

  add_item('ingredient', 'ingredients-list');
});

$("#add_cooking_method").click(function () {
  if(!$("#method").val()){
    $(".cooking_methods span").text("Cooking method must have a name");
    return;
  }

  add_item('method', 'cooking-methods-list');
});

/* Deletes the closest ingredient or cooking method */
$(".deleteListItem").click(function () {
  $(this).closest('li').remove();
});

/* Creates a new cooking method or ingredient list item and appends it to the appropiate list */
function add_item(item_id, item_list) {
  let newItem = document.getElementById(item_id);
  let itemsList = document.getElementsByClassName(item_list);

  let item = document.createElement('li');
  let itemP = document.createElement('p');
  let itemHiddenInput = document.createElement('input');

  let deleteItemButton = document.createElement('button');
  let iconDiv = document.createElement('div');
  let deleteIcon = document.createElement('i');

  itemP.innerText = newItem.value;

  itemHiddenInput.setAttribute("type", "hidden");
  itemHiddenInput.setAttribute("name", item_id + "s");
  itemHiddenInput.setAttribute("value", newItem.value);

  /* deleteItemButton.setAttribute("class", "deleteListItem"); */
  deleteItemButton.setAttribute("type", "button");
  deleteItemButton.setAttribute("class", "btn btn-unique btn-color btn-rounded btn-sm my-0");
  deleteIcon.setAttribute("class", "small material-icons");
  deleteIcon.innerText = "delete";

  iconDiv.appendChild(deleteIcon);
  deleteItemButton.appendChild(iconDiv);

  item.appendChild(itemP);
  item.appendChild(itemHiddenInput);
  item.appendChild(deleteItemButton);

  itemsList[0].appendChild(item);
  $('#' + item_id).val('');

  $(deleteItemButton).click(function () {
    $(this).closest('li').remove();
  });
}

/*
  Gives a preview of the image to be uploaded
  Credit to itsolutionstuff -
  https://www.itsolutionstuff.com/post/display-preview-selected-image-in-input-type-file-using-jqueryexample.html
*/

function readURL(input) {
  if (input.files && input.files[0]) {
    var reader = new FileReader();

    reader.onload = function (e) {
      $('#recipe_image').attr('src', e.target.result);
    }
    reader.readAsDataURL(input.files[0]);
  }
}
$("#image").change(function () {
  readURL(this);
});