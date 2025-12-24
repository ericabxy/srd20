---
title: SRD
groups:
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
---


<table>
<tr>
  <th colspan="2">System Reference Document</th>
</tr>
{% for group in page.groups %}
  <tr>
    <th>
      <a href="/{{ group.url }}">
        {{ group.name }}
      </a>
    </th>
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
