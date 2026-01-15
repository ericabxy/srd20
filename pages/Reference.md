---
layout: page
permalink: /Reference
title: Reference
---

> The System Reference Document is a comprehensive toolbox consisting of rules, races, classes, feats, skills, various systems, spells, magic items, and monsters compatible with the d20 System version of Dungeons & Dragons and various other roleplaying games from Wizards of the Coast.

Material published in the System Reference Document is considered Open Game Content under the Open Game License, and anyone may use, modify, and distribute it.

## Basic Rules and Legal

<p>
{% for post in site.basic_rules %}
  <a href='{{ post.url }}'>{{ post.title }}</a>
  {% unless forloop.last %}&bull;{% endunless %}
{% endfor %}
</p>

## Spells

<p>
{% for post in site.spells %}
  <a href='{{ post.url }}'>{{ post.title }}</a>
  {% unless forloop.last %}&bull;{% endunless %}
{% endfor %}
</p>

## Magic Items

<p>
{% for post in site.magic_items %}
  <a href='{{ post.url }}'>{{ post.title }}</a>
  {% unless forloop.last %}&bull;{% endunless %}
{% endfor %}
</p>

## Monsters

<p>
{% for post in site.monsters %}
  <a href='{{ post.url }}'>{{ post.title }}</a>
  {% unless forloop.last %}&bull;{% endunless %}
{% endfor %}
</p>

## Psionics

<p>
{% for post in site.psionics %}
  <a href='{{ post.url }}'>{{ post.title }}</a>
  {% unless forloop.last %}&bull;{% endunless %}
{% endfor %}
</p>

## Epic

<p>
{% for post in site.epic %}
  <a href='{{ post.url }}'>{{ post.title }}</a>
  {% unless forloop.last %}&bull;{% endunless %}
{% endfor %}
</p>

## Divine

<p>
{% for post in site.divine %}
  <a href='{{ post.url }}'>{{ post.title }}</a>
  {% unless forloop.last %}&bull;{% endunless %}
{% endfor %}
</p>

## Modern Basics

<p>
{% for post in site.modern_basics %}
  <a href='{{ post.url }}'>{{ post.title }}</a>
  {% unless forloop.last %}&bull;{% endunless %}
{% endfor %}
</p>

## Arcana

<p>
{% for post in site.arcana %}
  <a href='{{ post.url }}'>{{ post.title }}</a>
  {% unless forloop.last %}&bull;{% endunless %}
{% endfor %}
</p>

## Future

<p>
{% for post in site.future %}
  <a href='{{ post.url }}'>{{ post.title }}</a>
  {% unless forloop.last %}&bull;{% endunless %}
{% endfor %}
</p>

## Menaces

<p>
{% for post in site.menaces %}
  <a href='{{ post.url }}'>{{ post.title }}</a>
  {% unless forloop.last %}&bull;{% endunless %}
{% endfor %}
</p>
