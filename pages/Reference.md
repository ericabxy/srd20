---
layout: page
permalink: /Reference
title: Reference
---

> The System Reference Document is a comprehensive toolbox consisting of rules, races, classes, feats, skills, various systems, spells, magic items, and monsters compatible with the d20 System version of Dungeons & Dragons and various other roleplaying games from Wizards of the Coast.

Material published in the System Reference Document is considered Open Game Content under the Open Game License, and anyone may use, modify, and distribute it.

## System Reference Document

{% for group in site.data.grouped-srd %}
<h3>{{ group[0] }}</h3>
<p>
  {% for doc in group[1] %}
  <a href='{{ doc[1] }}'>{{ doc[0] }}</a>
  {% unless forloop.last %}&bull;{% endunless %}
  {% endfor %}
</p>
{% endfor %}

## Modern System Reference Document

{% for group in site.data.grouped-msrd %}
<h3>{{ group[0] }}</h3>
<p>
  {% for doc in group[1] %}
  <a href='{{ doc[1] }}'>{{ doc[0] }}</a>
  {% unless forloop.last %}&bull;{% endunless %}
  {% endfor %}
</p>
{% endfor %}
