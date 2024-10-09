---
layout: page
title: Obrazy
permalink: /obrazy/
---

<h2>Obrazy, které mám rád</h2>

<p>Občas mě zaujme nějaký obraz a udělám si poznámku. Tady. Třeba vás potěší, podívat se na hezký obraz. Nehledejte v tom větší smysl, než si říct něco k obrazu, který mne zaujal. Není v tom ani struktura podle období, ani snaha/možnost vám obraz prodat. Jediná struktura je, že jsem obraz viděl na vlastní oči v originále, tzn. zpravidla s ohledem na to, že jsem byl na výstavě, kde byl presentován.</p>

<table id="obrazy-table">
  <thead>
    <tr>
      <th onclick="sortTable(0)">Autor</th>
      <th onclick="sortTable(1)">Obraz</th>
      <th onclick="sortTable(2)">Styl</th>
      <th onclick="sortTable(3)">Namalováno</th>
    </tr>
  </thead>
  <tbody>
    {% assign unsorted_posts = site.obrazy | where_exp: "post", "post.order == nil" | sort: "date" | reverse %}
    {% for post in unsorted_posts %}
    <tr>
      <td>{{ post.autor }}</td>
      <td><a href="{{ post.url }}">{{ post.obraz }}</a></td>
      <td>{{ post.styl }}</td>
      <td>{{ post.namalovano }}</td>
    </tr>
    {% endfor %}
  </tbody>
</table>

<script>
function sortTable(n) {
  var table, rows, switching, i, x, y, shouldSwitch, dir, switchcount = 0;
  table = document.getElementById("obrazy-table");
  switching = true;
  dir = "asc";
  while (switching) {
    switching = false;
    rows = table.rows;
    for (i = 1; i < (rows.length - 1); i++) {
      shouldSwitch = false;
      x = rows[i].getElementsByTagName("TD")[n];
      y = rows[i + 1].getElementsByTagName("TD")[n];
      if (dir == "asc") {
        if (x.innerHTML.toLowerCase() > y.innerHTML.toLowerCase()) {
          shouldSwitch = true;
          break;
        }
      } else if (dir == "desc") {
        if (x.innerHTML.toLowerCase() < y.innerHTML.toLowerCase()) {
          shouldSwitch = true;
          break;
        }
      }
    }
    if (shouldSwitch) {
      rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
      switching = true;
      switchcount ++;
    } else {
      if (switchcount == 0 && dir == "asc") {
        dir = "desc";
        switching = true;
      }
    }
  }
}
</script>