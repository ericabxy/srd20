---
layout: post
title:  "Training a Creature"
date:   2026-01-31 12:55:00 -0800
categories: list
---

<ul>
{% for item in site.data.training-a-creature %}
  <li><a href='{{ item[1] }}'>{{ item[0] | capitalize }}</a></li>
{% endfor %}
</ul>
