---
layout: home
title: Graham 的数学花园
---

# 欢迎来到 Graham 的数学花园

系统性的数学知识整理与科普。

## 最新文章

{% for post in site.posts limit: 10 %}
- [{{ post.title }}]({{ post.url | relative_url }}) - {{ post.date | date: "%Y-%m-%d" }}
{% endfor %}
