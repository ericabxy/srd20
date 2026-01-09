---
permalink: /Special
title: Special
---

Special Abilities
=================

<ul>
{% for item in site.special_abilities %}
  <li>
    <a href='{{ item.url }}'>{{ item.title }}</a>
  </li>
{% endfor %}
</ul>
