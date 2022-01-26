---
layout: default
title: Archive
---

# Documentos Hackeados

<ul>
  {% assign tags = site.tags | sort 0 %}
  {% for tag_item in tags %}
  {% assign tag = (tag_item | first) %}
  <li>
    <a href="{{site.url}}{{site.baseurl}}/tags/{{tag}}">{{site.data.tags[tag].name}}</a> ({{site.tags[tag].size}})
  </li>
  {% endfor %}
</ul>

Browse all posts by month and year.

{% assign postsByYearMonth = site.posts | group_by_exp: "post", "post.date | date: '%B %Y'" %}
{% for yearMonth in postsByYearMonth %}
  <h2>{{ yearMonth.name }}</h2>
  <ul>
    {% for post in yearMonth.items %}
      <li><a href="{{ post.url }}">{{ post.title }}</a></li>
    {% endfor %}
  </ul>
{% endfor %}
