---
permalink: /scenarios
---

# Collection:Scenarios

<ul>
{% for doc in site.scenarios %}
  <li>
    <a href='{{ doc.url }}'>{{ doc.title }}</a>
  </li>
{% endfor %}
</ul>
