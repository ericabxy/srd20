---
title: Reference
---

{% for group in site.data.grouped-srd %}
<h2>{{ group[0] }}</h2>
  {% assign items = site.system | where: 'group', group[0] %}
<p>
  {% for item in items %}
  <a href="{{ item.url }}">{{ item.title }}</a>
    {% unless forloop.last %}&bull;{% endunless %}
  {% endfor %}
</p>
{% endfor %}

{% for group in site.data.grouped-msrd %}
<h2>{{ group[0] }}</h2>
  {% assign items = site.modern | where: 'group', group[0] %}
<p>
  {% for item in items %}
  <a href="{{ item.url }}">{{ item.title }}</a>
    {% unless forloop.last %}&bull;{% endunless %}
  {% endfor %}
</p>
{% endfor %}
