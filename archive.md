---
layout: default
title: 文章归档
---

<div class="page-header-simple">
  <h1>文章归档</h1>
</div>

<div class="archive-list">
  {% assign current_year = "" %}
  {% for post in site.posts %}
    {% assign post_year = post.date | date: "%Y" %}
    {% if post_year != current_year %}
      {% unless forloop.first %}</div>{% endunless %}
      <h2 class="archive-year">{{ post_year }}</h2>
      <div class="archive-posts">
      {% assign current_year = post_year %}
    {% endif %}
    <article class="archive-item">
      <time>{{ post.date | date: "%m-%d" }}</time>
      {% assign cat = post.categories | first %}
      {% if cat == 'number-theory' %}
        <span class="post-tag tag-number">数论</span>
      {% elsif cat == 'analysis' %}
        <span class="post-tag tag-analysis">分析</span>
      {% else %}
        <span class="post-tag tag-unsolved">未解</span>
      {% endif %}
      <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
    </article>
  {% endfor %}
  </div>
</div>
