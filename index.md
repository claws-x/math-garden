---
layout: home
title: 首页
---

<ul class="post-list">
  {% for post in site.posts limit: 15 %}
    {% assign tag_class = 'tag-unsolved' %}
    {% if post.categories contains 'number-theory' %}{% assign tag_class = 'tag-number' %}{% endif %}
    {% if post.categories contains 'analysis' %}{% assign tag_class = 'tag-analysis' %}{% endif %}
    <li class="post-item">
      <span class="post-date">{{ post.date | date: "%m / %d" }}</span>
      <div class="post-body">
        <span class="post-tag {{ tag_class }}">{{ post.categories | first | default: '未分类' }}</span>
        <h3><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h3>
        {% if post.excerpt %}
        <p class="post-excerpt">{{ post.excerpt | strip_html | truncate: 100 }}</p>
        {% endif %}
      </div>
    </li>
  {% endfor %}
</ul>
