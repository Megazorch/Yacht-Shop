// Assuming you have a button with id "plusButton" and an element to display the quantity with id "quantityDisplay"
var plusButton = document.getElementById('btn-plus');
var minusButton = document.getElementById('btn-minus')
var quantityDisplay = document.getElementById('var-value-my');
var cartlineitemId = document.getElementById('cartlineitem-id');


// Get the current quantity value
var currentQuantity = parseInt(quantityDisplay.textContent);

// Get the current cart line item id value
var currentCartLineItemId = parseInt(cartlineitemId.textContent);

// Update the quantity display by 1
var newQuantity = currentQuantity + 1;

function updateQuantity(currentCartLineItemId, currentQuantity) {
  var username = 'user1';
  var password = 'gaLAga123#';
  var url = '/catalog/cart-line-items/' + currentCartLineItemId + '/';

  var data = JSON.stringify({ quantity: currentQuantity });

  // Send the AJAX request
  var xhr = new XMLHttpRequest();
  xhr.open('PUT', url, true);
  xhr.setRequestHeader('Content-Type', 'application/json');

  // Construct the Authorization header
  var credentials = username + ':' + password;
  var encodedCredentials = btoa(credentials);
  xhr.setRequestHeader('Authorization', 'Basic ' + encodedCredentials);

  // Get the CSRF token value from the page's HTML
  var csrfToken = document.querySelector('input[name="csrfmiddlewaretoken"]').value;

  // Set the CSRF token in the request headers
  xhr.setRequestHeader('X-CSRFToken', csrfToken);

  xhr.onreadystatechange = function () {
    if (xhr.readyState === XMLHttpRequest.DONE) {
      if (xhr.status === 200) {
        // Reload the page after receiving a successful response
        location.reload();
      } else {
        console.error(xhr.responseText);
      }
    }
  };

  xhr.send(data);
};


function decreaseQuantity(currentCartLineItemId, currentQuantity) {
  if (currentQuantity > 1) {
    var newQuantity = currentQuantity - 1;
    updateQuantity(currentCartLineItemId, newQuantity);
  }
}

function increaseQuantity(currentCartLineItemId, currentQuantity) {
    var newQuantity = currentQuantity + 1;
  updateQuantity(currentCartLineItemId, newQuantity);
}

