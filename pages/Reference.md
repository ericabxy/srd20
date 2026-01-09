---
layout: page
permalink: /Reference
title: Reference
---

> The System Reference Document is a comprehensive toolbox consisting of rules, races, classes, feats, skills, various systems, spells, magic items, and monsters compatible with the d20 System version of Dungeons & Dragons and various other roleplaying games from Wizards of the Coast.

Material published in the System Reference Document is considered Open Game Content under the Open Game License, and anyone may use, modify, and distribute it.

## SRD

### Basic Rules and Legal

<p>
{% for post in site.categories['Basic Rules and Legal'] | sort_by: 'title' %}
  <a href='{{ post.url }}'>{{ post.title }}</a>
  {% unless forloop.last %}&bull;{% endunless %}
{% endfor %}
</p>

### Spells

<p>
{% for post in site.categories.Spells | sort_by: 'title' %}
  <a href='{{ post.url }}'>{{ post.title }}</a>
  {% unless forloop.last %}&bull;{% endunless %}
{% endfor %}
</p>

### Monsters

<p>
{% for post in site.categories.Monsters | sort_by: 'title' %}
  <a href='{{ post.url }}'>{{ post.title }}</a>
  {% unless forloop.last %}&bull;{% endunless %}
{% endfor %}
</p>

### Psionics

<p>
{% for post in site.categories.Psionics | sort_by: 'title' %}
  <a href='{{ post.url }}'>{{ post.title }}</a>
  {% unless forloop.last %}&bull;{% endunless %}
{% endfor %}
</p>

### Epic

<p>
{% for post in site.categories.Epic | sort_by: 'title' %}
  <a href='{{ post.url }}'>{{ post.title }}</a>
  {% unless forloop.last %}&bull;{% endunless %}
{% endfor %}
</p>

### Divine

<p>
{% for post in site.categories.Divine | sort_by: 'title' %}
  <a href='{{ post.url }}'>{{ post.title }}</a>
  {% unless forloop.last %}&bull;{% endunless %}
{% endfor %}
</p>

## MSRD

### Modern Basics

<p>
{% for post in site.categories['Modern Basics'] | sort_by: 'title' %}
  <a href='{{ post.url }}'>{{ post.title }}</a>
  {% unless forloop.last %}&bull;{% endunless %}
{% endfor %}
</p>

### Arcana

<p>
{% for post in site.categories.Arcana | sort_by: 'title' %}
  <a href='{{ post.url }}'>{{ post.title }}</a>
  {% unless forloop.last %}&bull;{% endunless %}
{% endfor %}
</p>

### Future

<p>
{% for post in site.categories.Future | sort_by: 'title' %}
  <a href='{{ post.url }}'>{{ post.title }}</a>
  {% unless forloop.last %}&bull;{% endunless %}
{% endfor %}
</p>

### Menaces

<p>
{% for post in site.categories.Menaces | sort_by: 'title' %}
  <a href='{{ post.url }}'>{{ post.title }}</a>
  {% unless forloop.last %}&bull;{% endunless %}
{% endfor %}
</p>
