---
layout: page
permalink: /SpecialAbilities
title: Special Abilities
---

A special ability grants a character the option to perform some particular feat, or otherwise grants the character some unusual quality. See [Special Abilities and Conditions](/AbilitiesandConditions) for details.

<h3>Extraordinary (Ex)</h3>

<p>
{% assign docs = site.special_abilities | where: "category", "extraordinary" %}
{% for doc in docs %}
  <a href='{{ doc.url }}'>{{ doc.title }}</a>
  {% unless forloop.last %}&bull;{% endunless %}
{% endfor %}
</p>

<h3>Spell-like (Sp)</h3>

<p>
{% assign docs = site.special_abilities | where: "category", "spell-like" %}
{% for doc in docs %}
  <a href='{{ doc.url }}'>{{ doc.title }}</a>
  {% unless forloop.last %}&bull;{% endunless %}
{% endfor %}
</p>

<h3>Supernatural (Su)</h3>

<p>
{% assign docs = site.special_abilities | where: "category", "supernatural" %}
{% for doc in docs %}
  <a href='{{ doc.url }}'>{{ doc.title }}</a>
  {% unless forloop.last %}&bull;{% endunless %}
{% endfor %}
</p>
