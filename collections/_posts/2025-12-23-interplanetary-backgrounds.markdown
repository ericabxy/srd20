---
layout: post
date:   2025-12-23 12:00:00 -0800
published: false
---

"Interplanetary" is a setting that spans the entire Solar System, encompassing hundreds of species and cultures populating every last planet and moon.

<table>
<tr>
<th colspan="2">Interplanetary</th>
</tr>
<tr>
<th>Backgrounds</th>
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
