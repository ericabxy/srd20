---
layout: post
title:  "Character Backgrounds"
date:   2025-12-23 00:00:00 -0800
---

"Races" in the SRD refers to a choice of genetic and cultural background for player characters. Race boils everything down to "racial" traits and bonuses, yet an elf raised away from traditional elven society is less likely to have an inherent affinity for martial weapons, and half-elves racial bonus to Diplomacy and Gather Information checks are more circumstantial than innate.

Genetic and cultural background is a fluid concept that can range from standard and stereotypical to unique and strange. These documents choose to refer to race instead as a character's "background" which can have genetic, cultural, and other components in an effort to interrogate and explore the potential of building your character's unique backstory.

<table>
<tr>
<th colspan="2">Character Backgrounds</th>
</tr>
<tr>
<th>Interplanetary</th>
<td>
{% for item in site.data.interplanetary-backgrounds %}
  <a href="{{ site.url }}{{ site.baseurl }}{{ item.url }}">
    {{ item.name }}
  </a>
  {% unless forloop.last %}&bull;{% endunless %}
{% endfor %}
</td>
</tr>
</table>
