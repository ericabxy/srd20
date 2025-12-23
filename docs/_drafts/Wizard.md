---
title: Wizard
permalink: wzzred
---

{% assign level = site.data.nth-level %}
{% assign bab = site.data.base-attack-bonus-poor %}
{% assign fort = site.data.save-bonus-poor %}
{% assign ref = site.data.save-bonus-poor %}
{% assign will = site.data.save-bonus-good %}
{% assign special = site.data.class-features-wizard %}

<table>
<caption>Table: The Wizard</caption>
<thead>
<tr>
  <th rowspan=2>Level</th>
  <th rowspan=2>Base Attack Bonus</th>
  <th rowspan=2>Fort Save</th>
  <th rowspan=2>Ref Save</th>
  <th rowspan=2>Will Save</th>
  <th rowspan=2>Special</th>
  <th colspan=10>Spells per Day</th>
</tr>
<tr>
  <th>0</th>
  <th>1st</th>
  <th>2nd</th>
  <th>3rd</th>
  <th>4th</th>
  <th>5th</th>
  <th>6th</th>
  <th>7th</th>
  <th>8th</th>
  <th>9th</th>
</tr>
</thead>
<tbody>
{% for nth in level %}
<tr>
  <td>{{ nth }}</td>
  <td>{{ bab[forloop.index0] }}</td>
  <td>{{ fort[forloop.index0] }}</td>
  <td>{{ ref[forloop.index0] }}</td>
  <td>{{ will[forloop.index0] }}</td>
  <td>{{ special[forloop.index0] }}</td>
</tr>
{% endfor %}
</tbody>
</table>
