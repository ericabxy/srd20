---
permalink: /Archetypes
title: Archetypes
---

<ul>
{% for item in site.archetypes %}
  <li>
    <a href='{{ item.url }}'>{{ item.title }}</a>
  </li>
{% endfor %}
</ul>
