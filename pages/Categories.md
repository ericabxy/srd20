---
permalink: /Categories
title: Categories
---

{% for category in site.categories %}
  <h3>{{ category[0] }}</h3>
  <p>
    {% for post in category[1] %}
      <a href="{{ post.url }}">{{ post.title }}</a>
      {% unless forloop.last %}&bull;{% endunless %}
    {% endfor %}
  </p>
{% endfor %}
