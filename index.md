---
title: Opinião de João Bosco Mota Amaral
layout: default
permalink: /
---
# Últimas
<ul>
  {% for post in site.posts %}
    <li>
      <a href="{{ post.url }}">{{ post.date | date: "%Y-%m-%d" }} - {{ post.title }}</a>
    </li>
  {% endfor %}
</ul>