---
title: SRD
---

<table>
<tr>
  <th colspan="2">System Reference Document</th>
</tr>
{% for group in site.data.grouped-srd %}
  <tr>
    <th>
      <a href="/{{ group[1] }}">
        {{ group[0] }}
      </a>
    </th>
    <td>
    {% assign docs = site.srd | where: 'parent', group[0] %}
    {% for doc in docs %}
      <a href="{{ site.url }}{{ site.baseurl }}{{ doc.url }}">
        {{ doc.title }}
      </a>
      {% unless forloop.last %}&bull;{% endunless %}
    {% endfor %}
    </td> 
  </tr>
{% endfor %}
<tr>
<th><a href="BasicRulesIndex">Basic Rules and Legal</a></th>
<td>
{% assign docs = site.srd | where: 'parent', 'Basic Rules and Legal' %}
{% for doc in docs %}
  <a href="{{ site.url }}{{ site.baseurl }}{{ doc.url }}">
    {{ doc.title }}
  </a>
  {% unless forloop.last %}&bull;{% endunless %}
{% endfor %}
</td>
</tr>
<tr>
<th><a href="SpellsIndex">Spells</a></th>
<td>
{% assign docs = site.srd | where: 'parent', 'Spells' %}
{% for doc in docs %}
  <a href="{{ site.url }}{{ site.baseurl }}{{ doc.url }}">
    {{ doc.title }}
  </a>
  {% unless forloop.last %}&bull;{% endunless %}
{% endfor %}
</td>
</tr>
<tr>
<th><a href="MagicItemsIndex">Magic Items</a></th>
<td>
{% assign docs = site.srd | where: 'parent', 'Magic Items' %}
{% for doc in docs %}
  <a href="{{ site.url }}{{ site.baseurl }}{{ doc.url }}">
    {{ doc.title }}
  </a>
  {% unless forloop.last %}&bull;{% endunless %}
{% endfor %}
</td>
</tr>
<tr>
<th><a href="MonstersIndex">Monsters</a></th>
<td>
{% assign docs = site.srd | where: 'parent', 'Monsters' %}
{% for doc in docs %}
  <a href="{{ site.url }}{{ site.baseurl }}{{ doc.url }}">
    {{ doc.title }}
  </a>
  {% unless forloop.last %}&bull;{% endunless %}
{% endfor %}
</td>
</tr>
<tr>
<th><a href="PsionicsIndex">Psionics</a></th>
<td>
{% assign docs = site.srd | where: 'parent', 'Psionics' %}
{% for doc in docs %}
  <a href="{{ site.url }}{{ site.baseurl }}{{ doc.url }}">
    {{ doc.title }}
  </a>
  {% unless forloop.last %}&bull;{% endunless %}
{% endfor %}
</td>
</tr>
<tr>
<th><a href="EpicIndex">Epic</a></th>
<td>
{% assign docs = site.srd | where: 'parent', 'Epic' %}
{% for doc in docs %}
  <a href="{{ site.url }}{{ site.baseurl }}{{ doc.url }}">
    {{ doc.title }}
  </a>
  {% unless forloop.last %}&bull;{% endunless %}
{% endfor %}
</td>
</tr>
<tr>
<th><a href="DivineIndex">Divine</a></th>
<td>
{% assign docs = site.srd | where: 'parent', 'Divine' %}
{% for doc in docs %}
  <a href="{{ site.url }}{{ site.baseurl }}{{ doc.url }}">
    {{ doc.title }}
  </a>
  {% unless forloop.last %}&bull;{% endunless %}
{% endfor %}
</td>
</tr>
</table>
