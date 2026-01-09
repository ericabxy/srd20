---
layout: post
categories: terminology
---

"Races" in the SRD refers to a choice of genetic and cultural background for player characters. Race boils everything down to "racial" traits and bonuses, yet an elf raised away from traditional elven society is less likely to have an inherent affinity for martial weapons, and half-elves racial bonus to Diplomacy and Gather Information checks are more circumstantial than innate.

Genetic and cultural background is a fluid concept that can range from standard and stereotypical to unique and strange. These documents sometimes refer to race instead as a character's "background" which can have genetic, cultural, and other components in an effort to interrogate and explore the potential of building your character's unique backstory.

The SRD offers seven races for players to choose as their background. The list of monsters reveals three more playable creatures with a +0 level adjustment, putting them on-par with the standard backgrounds and raising the total count to ten.

<table>
<tr>
<th colspan="2">Character Backgrounds</th>
</tr>
<tr>
<th>Standard</th>
<td>
{% for item in site.data.standard-backgrounds %}
  <a href="{{ site.url }}{{ site.baseurl }}{{ item.url }}">
    {{ item.name }}
  </a>
  {% unless forloop.last %}&bull;{% endunless %}
{% endfor %}
</td>
</tr>
</table>
