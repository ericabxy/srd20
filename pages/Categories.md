---
title: Categories
permalink: /categories
---

<table>
  <th>Backgrounds</th>
  <td>
{% for doc in site.backgrounds %}
  <a href='{{ doc.url }}'>{{ doc.title }}</a>
  {% unless forloop.last %}&bull;{% endunless %}
{% endfor %}
  </td>
</table>

<table>
  <th>Characters</th>
  <td>
{% for doc in site.characters %}
  <a href='{{ doc.url }}'>{{ doc.title }}</a>
  {% unless forloop.last %}&bull;{% endunless %}
{% endfor %}
  </td>
</table>

<table>
  <th>Locations</th>
  <td>
{% for doc in site.locations %}
  <a href='{{ doc.url }}'>{{ doc.title }}</a>
  {% unless forloop.last %}&bull;{% endunless %}
{% endfor %}
  </td>
</table>

<table>
  <th>Scenarios</th>
  <td>
{% for doc in site.scenarios %}
  <a href='{{ doc.url }}'>{{ doc.title }}</a>
  {% unless forloop.last %}&bull;{% endunless %}
{% endfor %}
  </td>
</table>
