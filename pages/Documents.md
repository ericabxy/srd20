---
permalink: /Documents
title: Documents
---

## Characters

<p>
{% for doc in site.characters %}
  <a href='{{ doc.url }}'>{{ doc.title }}</a>
  {% unless forloop.last %}&bull;{% endunless %}
{% endfor %}
</p>

## Locations

<p>
{% for doc in site.locations %}
  <a href='{{ doc.url }}'>{{ doc.title }}</a>
  {% unless forloop.last %}&bull;{% endunless %}
{% endfor %}
</p>
