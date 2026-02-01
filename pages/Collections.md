---
permalink: /Collections
title: Collections
---

Collections
===========

{% for collection in site.collections %}
<h2>{{ collection.label }}</h2>
<p>
  {% for item in collection.docs %}
  <a href='{{ item.url }}'>{{ item.title }}</a>
    {% unless forloop.last %}&bull;{% endunless %}
  {% endfor %}
</p>
{% endfor %}
