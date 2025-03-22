---
layout: null
---
(function() {
  function displaySearchResults(results, store) {
    var searchResults = document.getElementById('search-results');

    if (results.length) { // Are there any results?
      var appendString = '';

      for (var i = 0; i < results.length; i++) {  // Iterate over the results
        var item = store[results[i].ref];
        appendString += '<div class="search-result-item">';
        appendString += '<h3><a href="' + item.url + '">' + item.title + '</a></h3>';
        appendString += '<p>' + item.content.substring(0, 150) + '...</p>';
        appendString += '<div class="search-result-meta">';
        appendString += '<span class="search-result-category">' + item.category + '</span>';
        appendString += '<span class="search-result-date">' + item.date + '</span>';
        appendString += '</div>';
        appendString += '</div>';
      }

      searchResults.innerHTML = appendString;
    } else {
      searchResults.innerHTML = '<p>Nebyl nalezen žádný výsledek pro "<strong>' + searchTerm + '</strong>". Zkuste jiné klíčové slovo.</p>';
    }
  }

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

  var searchTerm = getQueryVariable('query');

  if (searchTerm) {
    document.getElementById('search-box').setAttribute("value", searchTerm);

    // Initialize lunr with Czech language support
    var idx = lunr(function () {
      this.use(lunr.cs); // Use Czech language support
      this.ref('id');
      this.field('title', { boost: 10 });
      this.field('category', { boost: 5 });
      this.field('tags', { boost: 5 });
      this.field('content');
      
      // Add documents to index
      for (var key in window.store) {
        this.add({
          'id': key,
          'title': window.store[key].title,
          'category': window.store[key].category,
          'tags': window.store[key].tags,
          'content': window.store[key].content
        });
      }
    });

    var results = idx.search(searchTerm); // Get lunr to perform a search
    displaySearchResults(results, window.store); // We'll write this in the next section
  }
})();