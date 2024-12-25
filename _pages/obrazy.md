---
layout: page
title: Obrazy
permalink: /obrazy/
---

<h2>Zajímavé obrazy - stručný průvodce</h2>

<p>Občas mě zaujme nějaký obraz a udělám si poznámku. Tady. Postupně se z poznámek stal příjemný přehled zajímavých obrazů z nejrůznějších výstav. Třeba potěší i vás.</p>

<table id="obrazy-table" style="border-collapse: separate; border-spacing: 10px; width: 100%;">
  <thead>
    <tr>
      <th onclick="sortTable(0)">Autor &#x25B2;&#x25BC;</th>
      <th onclick="sortTable(1)">Obraz &#x25B2;&#x25BC;</th>
      <th onclick="sortTable(3)">Rok &#x25B2;&#x25BC;</th>
      <th onclick="sortTable(2)">Styl &#x25B2;&#x25BC;</th>
    </tr>
  </thead>
  <tbody>
    {% assign unsorted_posts = site.obrazy | where_exp: "post", "post.order == nil" | sort: "date" | reverse %}
    {% for post in unsorted_posts %}
    <tr>
      <td><a href="{{ post.url }}">{{ post.autor }}</a></td>
      <td><a href="{{ post.url }}">{{ post.obraz }}</a></td>
      <td>{{ post.namalovano }}</td>
      <td>{{ post.styl }}</td>
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
