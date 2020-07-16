

/* Nav */

$(document).ready(function () {
  $('.sidenav').sidenav();
  $('select').formSelect();
});

$('.dropdown-trigger').dropdown();

$("#add_ingredient").click(function () {
  add_item('ingredient', 'ingredients-list');
});

$("#add_cooking_method").click(function () {
  add_item('method', 'cooking-methods-list');
});

/* $(".deleteListItem").click(function () {
  $(this).closest('li').remove();
}); */


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
  itemHiddenInput.setAttribute("name", item_id+"s");
  itemHiddenInput.setAttribute("value", newItem.value);
  
  /* deleteItemButton.setAttribute("class", "deleteListItem"); */
  deleteItemButton.setAttribute("type", "button");

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
$("#image").change(function(){
  readURL(this);
});