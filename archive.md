---
layout: default
title: 文章归档
---

<h1 class="page-title">文章归档</h1>

<div class="archive-list">
  {% for post in site.posts %}
    {% assign current_year = post.date | date: "%Y" %}
    {% if current_year != year %}
      {% if year %}</div>{% endif %}
      <h2 class="archive-year">{{ current_year }}</h2>
      <div class="archive-posts">
      {% assign year = current_year %}
    {% endif %}
    <article class="archive-item">
      <time>{{ post.date | date: "%Y-%m-%d" }}</time>
      <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
      {% if post.subtitle %}
        <span class="post-subtitle">{{ post.subtitle }}</span>
      {% endif %}
    </article>
  {% endfor %}
  </div>
</div>
