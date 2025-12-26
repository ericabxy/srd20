---
title: Reference
srd:
- name: Basic Rules and Legal
  url: BasicRules
- name: Spells
  url: Spells
- name: Magic Items
  url: MagicItems
- name: Monsters
  url: Monsters
- name: Psionics
  url: Psionics
- name: Epic
  url: Epic
- name: Divine
  url: Divine
msrd:
- name: Modern Basics
  url: ModernBasics
- name: Arcana
  url: Arcana
- name: Future
  url: Future
- name: Menaces
  url: Menaces
---

<table>
<tr><th colspan="2">System Reference Document</th></tr>
{% for group in page.srd %}
<tr>
<th>{{ group.name }}</th>
<td>
{% assign docs = site.reference | where: 'parent', group.name %}
{% for doc in docs %}
  <a href="{{ site.url }}{{ site.baseurl }}{{ doc.url }}">
    {{ doc.title }}
  </a>
  {% unless forloop.last %}&bull;{% endunless %}
{% endfor %}
</td> 
</tr>
{% endfor %}
<tr><th colspan="2">Modern System Reference Document</th></tr>
{% for group in page.msrd %}
<tr>
<th>{{ group.name }}</th>
<td>
{% assign docs = site.reference | where: 'parent', group.name %}
{% for doc in docs %}
  <a href="{{ site.url }}{{ site.baseurl }}{{ doc.url }}">
    {{ doc.title }}
  </a>
  {% unless forloop.last %}&bull;{% endunless %}
{% endfor %}
</td> 
</tr>
{% endfor %}
</table>
