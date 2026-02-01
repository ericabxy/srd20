---
layout: post
title: Creatures
date: 2026-01-31 12:52 -0800
---

<p>
  <span>Creatures are playable and non-playable entities with ability scores and derived statistics. Find creatures by their alphabetized name:</span> 
{% for group in site.data.alphabetical-listing-of-monsters %}
  <a href='#{{ group[0] }}'>{{ group[0] | capitalize }}</a>
  {% if forloop.last %}.{% endif %}
{% endfor %}
</p>

<p>Some creatures can be played <a href='#as-characters'>as characters</a>.</p>

<p>Some creatures can be trained <a href='#training-a'>as mounts</a>.</p>

{% for group in site.data.alphabetical-listing-of-monsters %}
<h2 id='{{ group[0] }}'>{{ group[0] }}</h2>

<ul>
  {% for item in group[1] %}
  <li><a href='{{ item[1] }}'>{{ item[0] | capitalize }}</a></li>
  {% endfor %}
</ul>
{% endfor %}

<h2 id='as-characters'>Characters</h2>

<ul>
{% for item in site.data.creatures-as-characters %}
  <li><a href='{{ item[1] }}'>{{ item[0] | capitalize }}</a></li>
{% endfor %}
</ul>

<h2 id='training-a'>Training</h2>

<ul>
{% for item in site.data.training-a-creature %}
  <li><a href='{{ item[1] }}'>{{ item[0] | capitalize }}</a></li>
{% endfor %}
</ul>
