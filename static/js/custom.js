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

  var url = '/catalog/cart-line-items/' + currentCartLineItemId + '/';

  var data = JSON.stringify({ quantity: currentQuantity });

  // Send the AJAX request
  var xhr = new XMLHttpRequest();
  xhr.open('PUT', url, true);
  xhr.setRequestHeader('Content-Type', 'application/json');

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

// Add event listener to delete button
$('.delete-button').click(function() {
  var lineItemId = $(this).data('line-item-id');
  deleteCartLineItem(lineItemId);
});

// Function to send AJAX request to delete cart line item
function deleteCartLineItem(lineItemId) {
  // Create an XMLHttpRequest object
  var xhr = new XMLHttpRequest();

  // Set up the request
  xhr.open('DELETE', '/catalog/cart-line-items/' + lineItemId + '/');

  // Get the CSRF token from the cookie
  var csrftoken = document.querySelector('input[name="csrfmiddlewaretoken"]').value;

  // Set the CSRF token in the request header
  xhr.setRequestHeader('X-CSRFToken', csrftoken);

  // Set the callback function to handle the response
  xhr.onload = function() {
    if (xhr.status === 204) {
      /// Reload the page after a short delay
      setTimeout(function() {
        location.reload();
      }, 500); // Adjust the delay as needed
    } else {
      console.error('Request failed. Status: ' + xhr.status);
    }
  };

  // Send the request
  xhr.send();
}
