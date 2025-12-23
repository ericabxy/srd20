---
title: MSRD
---

<table>
<tr>
  <th colspan="2">Modern System Reference Document</th>
</tr>
<tr>
<th><a href="modernbasicsindex">Modern Basics</a></th>
<td>
{% assign docs = site.msrd | where: 'parent', 'Modern Basics' %}
{% for doc in docs %}
  <a href="{{ site.url }}{{ site.baseurl }}{{ doc.url }}">
    {{ doc.title }}
  </a>
  {% unless forloop.last %}&bull;{% endunless %}
{% endfor %}
</td>
</tr>
<tr>
<th><a href="ArcanaIndex">Arcana</a></th>
<td>
{% assign docs = site.msrd | where: 'parent', 'Arcana' %}
{% for doc in docs %}
  <a href="{{ site.url }}{{ site.baseurl }}{{ doc.url }}">
    {{ doc.title }}
  </a>
  {% unless forloop.last %}&bull;{% endunless %}
{% endfor %}
</td>
</tr>
<tr>
<th><a href="FutureIndex">Future</a></th>
<td>
{% assign docs = site.msrd | where: 'parent', 'Future' %}
{% for doc in docs %}
  <a href="{{ site.url }}{{ site.baseurl }}{{ doc.url }}">
    {{ doc.title }}
  </a>
  {% unless forloop.last %}&bull;{% endunless %}
{% endfor %}
</td>
</tr>
<tr>
<th><a href="MenacesIndex">Menaces</a></th>
<td>
{% assign docs = site.msrd | where: 'parent', 'Menaces' %}
{% for doc in docs %}
  <a href="{{ site.url }}{{ site.baseurl }}{{ doc.url }}">
    {{ doc.title }}
  </a>
  {% unless forloop.last %}&bull;{% endunless %}
{% endfor %}
</td>
</tr>
</table>
