---
title: SRD20, the documentation project
---

{{ site.baseurl }}

Welcome to SRD20, a free role-playing game documentation project.

{% include special-abilities.html %}

{% include rules-variants.html %}

Backgrounds
-----------

{% include character-backgrounds.html %}

<table>
<tr>
<th>Character Backgrounds</th>
<td>
{% for doc in site.pages %}
  {% if doc.category == "character-background" %}
    <a href="{{ doc.url }}">{{ doc.title }}</a>
    {% unless forloop.last %}&bull;{% endunless %}
  {% endif %}
{% endfor %}
</td>
</tr>
</table>

Open Game Content References
----------------------------

{% include system-reference-document.html %}

{% include modern-system-reference-document.html %}

{% include arcana-unearthed.html %}

External Links
--------------

- [Revised (v.3.5) System Reference Document](http://web.archive.org/web/20060819135437/http://www.wizards.com/default.asp?x=d20/article/srd35)(archived August 19th, 2006) 
- [d20 Modern System Reference Document](http://web.archive.org/web/20060819135213/http://www.wizards.com/default.asp?x=d20/article/msrd)(archived August 19th, 2006)
- [Archives of Nethys - Pathfinder RPG Database](https://www.aonprd.com/)
- [Archives of Nethys - Starfinder RPG Database](https://www.aonsrd.com/)
- [d20 System Reference Document 3.0](http://www.dragon.ee/30srd/)
- [The Hypertext d20 SRD](https://www.d20srd.org/index.htm)
