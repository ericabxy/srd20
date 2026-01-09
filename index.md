---
layout: home
list_title: Latest Posts
---

SRD20 is a collection of experiments based on a 2003 tabletop role-playing game system. Each experiment is designed as a complete and self-contained artifact, intentionally small and limited in scope.

{{ site.arcana | size }}
{% for item in site.arcana %}
  {{ item.title }}
{% endfor %}
