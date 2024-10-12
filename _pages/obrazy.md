---
layout: page
title: Obrazy
permalink: /obrazy/
---

<h2>Obrazy, které mám rád</h2>

<p>Občas mě zaujme nějaký obraz a udělám si poznámku. Tady. Třeba vás potěší, podívat se na hezký obraz. Nehledejte v tom větší smysl, než si říct něco k obrazu, který mne zaujal. Není v tom ani struktura podle období, ani snaha/možnost vám obraz prodat. Jediná struktura je, že jsem obraz viděl na vlastní oči v originále, tzn. zpravidla s ohledem na to, že jsem byl na výstavě, kde byl presentován.</p>

<table id="obrazy-table" style="border-collapse: separate; border-spacing: 10px; width: 100%;">
  <thead>
    <tr>
      <th onclick="sortTable(0)">Autor &#x25B2;&#x25BC;</th>
      <th onclick="sortTable(1)">Obraz &#x25B2;&#x25BC;</th>
      <th onclick="sortTable(3)">Namalováno &#x25B2;&#x25BC;</th>
      <th onclick="sortTable(2)">Styl &#x25B2;&#x25BC;</th>
    </tr>
  </thead>
  <tbody>
    {% assign unsorted_posts = site.obrazy | where_exp: "post", "post.order == nil" | sort: "date" | reverse %}
    {% for post in unsorted_posts %}
    <tr>
      <td>{{ post.autor }}</td>
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

<h1>Dominantní barvy</h1>
<img id="image" src="https://res.cloudinary.com/dvwv5cne3/image/fetch/w_300,h_300,c_fill/https://www.marigold.cz/assets/obrazy/tanguy-promontory-palace.jpg" alt="Image" width="300">
<div id="color-palette"></div>

<style>
  .color-box {
      width: 100px;
      height: 100px;
      display: inline-block;
      margin: 5px;
      border-radius: 10px;  /* Zaoblené rohy */
      border: 2px solid #000;  /* Černý okraj */
  }
</style>

<script>
    document.addEventListener('DOMContentLoaded', function() {
        const externalImageUrl = encodeURIComponent("https://www.marigold.cz/assets/obrazy/tanguy-promontory-palace.jpg");
        const cloudName = "dvwv5cne3";

        async function getDominantColors() {
            const url = `https://res.cloudinary.com/${cloudName}/image/fetch/fl_getinfo/${externalImageUrl}`;
            try {
                const response = await fetch(url);
                if (!response.ok) {
                    throw new Error(`HTTP error! status: ${response.status}`);
                }
                const data = await response.json();

                const colorPalette = document.getElementById('color-palette');
                if (data.colors) {
                    data.colors.forEach(colorObj => {
                        const colorBox = document.createElement('div');
                        colorBox.className = 'color-box';
                        colorBox.style.backgroundColor = colorObj.color;
                        colorPalette.appendChild(colorBox);
                    });
                } else {
                    console.error('Žádné barvy nebyly vráceny pro obrázek.');
                }
            } catch (error) {
                console.error('Chyba při získávání barev:', error);
            }
        }

        getDominantColors();
    });
</script>