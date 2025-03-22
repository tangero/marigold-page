// Připraven počkat na načtení dokumentu
document.addEventListener('DOMContentLoaded', function() {
  // Získání parametru z URL
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
    return String(text).toLowerCase()
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
        
        // Bezpečné zobrazení obsahu
        var content = item.content || '';
        if (content.length > 150) {
          content = content.substring(0, 150) + '...';
        }
        appendString += '<p>' + content + '</p>';
        
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
    var searchBox = document.getElementById('search-box');
    if (searchBox) {
      searchBox.setAttribute("value", searchTerm);
    }
    
    try {
      // Ensure we have a valid store object
      if (typeof window.store !== 'object') {
        console.error("Store object is not available or not an object");
        return;
      }
    
      // Normalize the search term
      var normalizedSearchTerm = normalizeText(searchTerm);
      
      // Array to store the results
      var results = [];
      
      // For each item in the store
      for (var key in window.store) {
        try {
          // Skip if not a direct property or null
          if (!window.store.hasOwnProperty(key) || !window.store[key]) continue;
          
          var item = window.store[key];
          
          // Get the title, content and tags
          var title = normalizeText(item.title || '');
          var content = normalizeText(item.content || '');
          var tags = normalizeText(item.tags || '');
          var category = normalizeText(item.category || '');
          
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
            try {
              var regex = new RegExp(normalizedSearchTerm, 'gi');
              var matches = content.match(regex);
              if (matches) {
                score += Math.min(matches.length, 10); // Cap at 10 additional points
              }
            } catch(e) {
              console.error("Error in regex matching:", e);
            }
          }
          
          // If the score is greater than 0, add it to the results
          if (score > 0) {
            results.push({
              ref: key,
              score: score
            });
          }
        } catch(e) {
          console.error("Error processing item:", key, e);
        }
      }
      
      // Sort the results by score
      results.sort(function(a, b) {
        return b.score - a.score;
      });
      
      // Display the results
      displaySearchResults(results, window.store);
    } catch(e) {
      console.error("Error during search:", e);
      var searchResults = document.getElementById('search-results');
      searchResults.innerHTML = '<p>Nastala chyba při vyhledávání. Zkuste to prosím později.</p>';
    }
  }
});