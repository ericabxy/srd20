---
layout: page
permalink: /Collections
title: Collections
---

### Backgrounds

<p>
{% for doc in site.backgrounds %}
  <a href='{{ doc.url }}'>{{ doc.title }}</a>
  {% unless forloop.last %}&bull;{% endunless %}
{% endfor %}
</p>

### Characters

<p>
{% for doc in site.characters %}
  <a href='{{ doc.url }}'>{{ doc.title }}</a>
  {% unless forloop.last %}&bull;{% endunless %}
{% endfor %}
</p>

### Locations

<p>
{% for doc in site.locations %}
  <a href='{{ doc.url }}'>{{ doc.title }}</a>
  {% unless forloop.last %}&bull;{% endunless %}
{% endfor %}
</p>

### Scenarios

<p>
{% for doc in site.scenarios %}
  <a href='{{ doc.url }}'>{{ doc.title }}</a>
  {% unless forloop.last %}&bull;{% endunless %}
{% endfor %}
</p>
