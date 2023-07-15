// Get the current URL
    var currentUrl = window.location.href;

// Get the select element
    const selectElement = document.getElementById('sort_option');

// Get the selected option value from the query parameters
    const urlParams = new URLSearchParams(window.location.search);
    const selectedOption = urlParams.get('sort');

// Set the selected attribute for the corresponding option
    Array.from(selectElement.options).forEach(option => {
        if (option.value === selectedOption) {
          option.setAttribute('selected', 'selected');
        }
    });

// Add an event listener to listen for changes
    selectElement.addEventListener('change', function() {
// Get the selected option value
    const selectedOption = selectElement.value;

// Check if the URL already has a query string
    if (currentUrl.indexOf('?') !== -1) {
      /// URL already has a query string
      var searchParams = new URLSearchParams(window.location.search);

      // Update or add the 'sort' parameter
      searchParams.set('sort', selectedOption);

      // Get the updated search string
      var updatedSearchString = searchParams.toString();

      // Update the URL with the updated search string
      var updatedUrl = currentUrl.split('?')[0] + '?' + updatedSearchString;
    } else {
      // URL does not have any query string, add the 'sort' parameter
      var updatedUrl = currentUrl + '?sort=' + selectedOption;
    }

// Redirect to the desired URL based on the selected option
    window.location.href = updatedUrl;
});