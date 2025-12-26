---
title: Special Abilities
---

# Special Ability

All class features are being translated into special abilities that can be "taken" as part of character creation and character advancement, similar to [fighter](/ClassesI#fighter) bonus feats and [rogue](/ClassesII#rogue) special abilities.

<table>
<tr><th colspan="2">Special Abilities</th></tr>
<tr><th>Extraordinary</th><td>
{% assign docs = site.special_abilities | where_exp: 'item', 'item.categories contains "extraordinary ability"' %}
{% for doc in docs %}
  <a href="{{ doc.url }}">{{ doc.title }}</a>
  {% unless forloop.last %}&bull;{% endunless %}
{% endfor %}
</td></tr>
<tr><th>Spell-like</th><td>
{% assign docs = site.special_abilities | where_exp: 'item', 'item.categories contains "spell-like ability"' %}
{% for doc in docs %}
  <a href="{{ doc.url }}">{{ doc.title }}</a>
  {% unless forloop.last %}&bull;{% endunless %}
{% endfor %}
</td></tr>
<tr><th>Supernatural</th><td>
{% assign docs = site.special_abilities | where_exp: 'item', 'item.categories contains "supernatural ability"' %}
{% for doc in docs %}
  <a href="{{ doc.url }}">{{ doc.title }}</a>
  {% unless forloop.last %}&bull;{% endunless %}
{% endfor %}
</td></tr>
</table>
