---
layout: null
---
(function() {
  // Get the query parameter
  function getQueryVariable(variable) {
    var query = window.location.search.substring(1);
    var vars = query.split('&');

    for (var i = 0; i < vars.length; i++) {
      var pair = vars[i].split('=');

      if (pair[0] === variable) {
        return decodeURIComponent(pair[1].replace(/\+/g, '%20'));
      }
    }
  }

  // Normalize text for search (lowercase, remove diacritics)
  function normalizeText(text) {
    if (!text) return '';
    return text.toLowerCase()
      .normalize("NFD")
      .replace(/[\u0300-\u036f]/g, "");
  }

  // Function to display search results
  function displaySearchResults(results, store) {
    var searchResults = document.getElementById('search-results');

    if (results.length) {
      var appendString = '';

      for (var i = 0; i < results.length; i++) {
        var item = store[results[i].ref];
        appendString += '<div class="search-result-item">';
        appendString += '<h3><a href="' + item.url + '">' + item.title + '</a></h3>';
        appendString += '<p>' + (item.content ? item.content.substring(0, 150) + '...' : '') + '</p>';
        appendString += '<div class="search-result-meta">';
        if (item.category) {
          appendString += '<span class="search-result-category">' + item.category + '</span>';
        }
        if (item.date) {
          appendString += '<span class="search-result-date">' + item.date + '</span>';
        }
        appendString += '</div>';
        appendString += '</div>';
      }

      searchResults.innerHTML = appendString;
    } else {
      searchResults.innerHTML = '<p>Nebyl nalezen žádný výsledek pro "<strong>' + searchTerm + '</strong>". Zkuste jiné klíčové slovo.</p>';
    }
  }

  // Get the search term from the URL
  var searchTerm = getQueryVariable('query');

  if (searchTerm) {
    // Set the search box value to the search term
    document.getElementById('search-box').setAttribute("value", searchTerm);
    
    // Normalize the search term
    var normalizedSearchTerm = normalizeText(searchTerm);
    
    // Array to store the results
    var results = [];
    
    // For each item in the store
    for (var key in window.store) {
      // Get the title, content and tags
      var title = normalizeText(window.store[key].title);
      var content = normalizeText(window.store[key].content);
      var tags = normalizeText(window.store[key].tags);
      var category = normalizeText(window.store[key].category);
      
      // Calculate a score based on how many times the search term appears
      var score = 0;
      
      // Check if the title contains the search term (worth more points)
      if (title.indexOf(normalizedSearchTerm) !== -1) {
        score += 10;
      }
      
      // Check if tags contain the search term
      if (tags && tags.indexOf(normalizedSearchTerm) !== -1) {
        score += 5;
      }
      
      // Check if category contains the search term
      if (category && category.indexOf(normalizedSearchTerm) !== -1) {
        score += 3;
      }
      
      // Check if the content contains the search term
      if (content && content.indexOf(normalizedSearchTerm) !== -1) {
        score += 1;
        
        // More points for more occurrences
        var regex = new RegExp(normalizedSearchTerm, 'gi');
        var matches = content.match(regex);
        if (matches) {
          score += Math.min(matches.length, 10); // Cap at 10 additional points
        }
      }
      
      // If the score is greater than 0, add it to the results
      if (score > 0) {
        results.push({
          ref: key,
          score: score
        });
      }
    }
    
    // Sort the results by score
    results.sort(function(a, b) {
      return b.score - a.score;
    });
    
    // Display the results
    displaySearchResults(results, window.store);
  }
})();