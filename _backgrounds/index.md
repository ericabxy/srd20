---
permalink: /backgrounds
---

# Collection:Backgrounds

<ul>
{% for doc in site.backgrounds %}
  <li>
    <a href='{{ doc.url }}'>{{ doc.title }}</a>
  </li>
{% endfor %}
</ul>
