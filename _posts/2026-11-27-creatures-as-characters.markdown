---
layout: post
title:  "Creatures as Characters"
date:   2026-01-31 12:51:00 -0800
categories: list
---

<ul>
{% for item in site.data.creatures-as-characters %}
  <li><a href='{{ item[1] }}'>{{ item[0] | capitalize }}</a></li>
{% endfor %}
</ul>
