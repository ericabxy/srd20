---
layout: post
date:   2025-12-23 11:00:00 -0800
categories: collection
---

This is a list of spells which can be made permanent with the a [*permanency*](/SpellsP-R#permanency) spell, an interesting worldbuilding effect that can be performed by spellcasters as low as caster level 9th.

<ul>
{% for spell in site.data.permanent-magic %}
  <li>
    <a href="{{ spell[1].url }}">
      {{ spell[0] }} ({{ spell[1].target }})
    </a>
  </li>
{% endfor %}
</ul>
